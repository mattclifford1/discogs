from topics import get_topics
from percent_genres import genre_percentages
from genre_add import make_even
import pandas as pd

from joblib import Parallel, delayed
import multiprocessing
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC

from classify_svm import split_data
from sklearn.utils import shuffle

def train_test(i,partitions,features,labels,clf):
	features_train, labels_train, features_test, labels_test = split_data(i, partitions, features, labels)
	clf.fit(features_train, labels_train)
	score = clf.score(features_test, labels_test)
	print(i, ': ',end=' ')
	print(score)

num_cores = multiprocessing.cpu_count()

topics = [4,6,8,10,14,18,22,26,30,35,40,50,60,70,90,110]
lyrics = pd.read_pickle('lyrics_genre_overlap.pkl')
genre_percentages(lyrics)
#make genres even
lyrics =  make_even(lyrics, max_number = 134, reduce_genres = ['Rock','Pop','Folk, World, & Country', 'Hip Hop','Electronic'])
genre_percentages(lyrics)
classifiers = [
	MLPClassifier(alpha=1,max_iter=500),
	SVC(gamma=2, C=1)]
names = ['SVM','neural network']
for i in topics:
	print('--------' + str(i) + '--------')
	features_df = get_topics(lyrics, i)
	print('|')
	labels = features_df['discogs_genre'].tolist()

	#get rid of genres column for training
	features_df =features_df.drop('discogs_genre',1)
	features = features_df.values.tolist()

	partitions = 4

	features, labels = shuffle(features, labels) #incase labels are in some order
	for name, clf in zip(names, classifiers):
		print(name)
		for i in range(partitions):
			train_test(i,partitions,features,labels,clf)
		# Parallel(n_jobs=num_cores)(delayed(train_test)(i,partitions,features,labels,clf) for i in range(partitions))

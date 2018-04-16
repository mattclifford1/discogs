import pickle
from classify_svm import split_data
import numpy as np
import pandas as pd
from sklearn.utils import shuffle
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

from joblib import Parallel, delayed
import multiprocessing
from percent_genres import genre_percentages
from genre_add import make_even

def train_test(i,partitions,features,labels,clf):
	features_train, labels_train, features_test, labels_test = split_data(i, partitions, features, labels)
	clf.fit(features_train, labels_train)
	score = clf.score(features_test, labels_test)
	print(i, ': ',end=' ')
	print(score)


num_cores = multiprocessing.cpu_count()

classifiers = [
	KNeighborsClassifier(3),
	SVC(kernel="linear", C=0.025),
	SVC(gamma=2, C=1),
	
	DecisionTreeClassifier(max_depth=5),
	RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
	MLPClassifier(alpha=1,max_iter=500),
	AdaBoostClassifier(),
	GaussianNB(),
	QuadraticDiscriminantAnalysis(),
	GaussianProcessClassifier(1.0 * RBF(1.0))]
names = ["Nearest Neighbors", "Linear SVM", "RBF SVM",
		 "Decision Tree", "Random Forest", "Neural Network", "AdaBoost",
		 "Naive Bayes", "QDA","Gaussian Process"]


features_df = pd.read_pickle('bag_of_words.pkl')
features_df = pd.read_pickle('topics_features_df.pkl')
genre_percentages(features_df) #prints the occurances of each genre

features_df =  make_even(features_df, max_number = 134, reduce_genres = ['Rock','Pop','Folk, World, & Country', 'Hip Hop','Electronic'])
labels = features_df['discogs_genre'].tolist()
genre_percentages(features_df)

#get rid of genres column for training
features_df =features_df.drop('discogs_genre',1)
features = features_df.values.tolist()

partitions = 4

features, labels = shuffle(features, labels) #incase labels are in some order
for name, clf in zip(names, classifiers):
	print(name)
	Parallel(n_jobs=num_cores)(delayed(train_test)(i,partitions,features,labels,clf) for i in range(partitions))
	# for i in range(partitions):
	# 	features_train, labels_train, features_test, labels_test = split_data(i, partitions, features, labels)
	# 	clf.fit(features_train, labels_train)
	# 	score = clf.score(features_test, labels_test)
	# 	print(score)







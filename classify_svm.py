from sklearn import svm
import numpy as np
import pickle
import pandas as pd

def split_data(it, part, features, labels):  #split train and test cycles
	feature = list(np.copy(features))  #for dumb python pointers, why would that be a feature lol?
	label = list(np.copy(labels))

	lower = int((it*len(label))/part)
	upper = int(((it+1)*len(label))/part)

	features_test = feature[lower:upper]
	labels_test = label[lower:upper]

	feature[lower:upper] = []   #train
	label[lower:upper] = []     #train

	return feature, label, features_test, labels_test

def train_classify(features, labels, partitions):  #need to both be lists, features is list of feature values for each item
	#find labels
	unique = list(set(labels))

	#dictionary for int to string label
	int_labels = [0]*len(labels)

	#assign string label to interger equivelant
	for i in range(len(labels)):
		int_labels[i] = unique.index(labels[i])  

	#cross validation showing correct classification (hard)
	for i in range(partitions):
		#get test/train partition from current cycle
		features_train, labels_train, features_test, labels_test = split_data(i, partitions, features, labels)
		
		clf = svm.SVC()       #define classifier
		clf.fit(features_train, labels_train)    #fit classifier to features

		#determine classification success
		correct = 0 
		incorrect = 0
		for i in range(len(labels_test)):
			prediction = clf.predict([features_test[i]]) #predict one test point from classifier
			if prediction == labels_test[i]:     #test if correct
				correct += 1
			else:
				incorrect +=1

		# print(str(correct) + ' correct')
		# print(str(incorrect) + ' incorrect')
		print(str(int((correct/(incorrect+correct))*100)) + '%' + ' success')

if __name__ == "__main__":
	###### train and classify different data 
	partitions = 4    #cycles of cross validation
	print('---------bag of words----------')
	features_df = pd.read_pickle('even_bag_of_words.pkl')
	features = features_df.values.tolist()
	labels = pickle.load(open('even_lyrics_genres.pkl', 'rb'))  #same for both lyrics sets
	train_classify(features, labels, partitions)

	print('---------topic model-----------')
	#load labeled data for lyric topics
	features2 = list(np.load('features.npy'))
	#train and test classifer
	train_classify(features2, labels, partitions)


	# print('--------combined lyrics--------')

	# df = pd.read_pickle('topics_features_df.pkl')
	# comb_data = pd.concat([features_df, df], axis=1)
	# comb_data = comb_data.values.tolist()
	# train_classify(comb_data, labels, partitions)

	print('---------timbre data-----------')
	#load labeled data for basic timbre features
	# features3 = pickle.load(open('filtered_features.pkl', 'rb'), encoding='latin1')
	features3 = pickle.load(open('filtered_features.pkl', 'rb'))
	# features3 = features.values.tolist()   #turn pandas df to 2d array
	labels3 = pickle.load(open('classes.pkl', 'rb')).tolist()
	#train and test classifer
	train_classify(features3, labels3, partitions)



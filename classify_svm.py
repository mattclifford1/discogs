from sklearn import svm
import numpy as np
import pickle

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

#load labels data
features = list(np.load('features.npy'))
labels = pickle.load(open('lyrics_genres.pkl', 'rb'))

#find labels
unique = list(set(labels))

#dictionary for int to string label
int_labels = [0]*len(labels)

#assign string label to interger equivelant
for i in range(len(labels)):
	int_labels[i] = unique.index(labels[i])  

#cross validation showing correct classification (hard)
partitions = 10
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

from sklearn import svm
import numpy as np
import pickle

features = np.load('features.npy')
labels = pickle.load(open('lyrics_genres.pkl', 'rb'))

unique = list(set(labels))

int_labels = [0]*len(labels)

for i in range(len(labels)):
	int_labels[i] = unique.index(labels[i])  #assign string label to interger equivelant

#split into test and train
lim = int(4*len(labels)/5)
train_features = features[:lim]
test_features = features[lim:]

train_labels = int_labels[:lim]
test_labels = int_labels[lim:]

clf = svm.SVC()
clf.fit(train_features, train_labels) 

correct = 0 
incorrect = 0
for i in range(len(test_labels)):
	prediction = clf.predict([test_features[i]])
	if prediction == test_labels[i]:
		correct += 1
	else:
		incorrect +=1

print(str(correct) + ' correct')
print(str(incorrect) + ' incorrect')
print(str((correct/(incorrect+correct))*100) + '\%' + ' success')
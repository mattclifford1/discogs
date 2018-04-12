import pickle
from classify_svm import split_data
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
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
num_cores = multiprocessing.cpu_count()

classifiers = [
	KNeighborsClassifier(3),
	SVC(kernel="linear", C=0.025),
	SVC(gamma=2, C=1),
	GaussianProcessClassifier(1.0 * RBF(1.0)),
	DecisionTreeClassifier(max_depth=5),
	RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
	MLPClassifier(alpha=1),
	AdaBoostClassifier(),
	GaussianNB(),
	QuadraticDiscriminantAnalysis()]
names = ["Nearest Neighbors", "Linear SVM", "RBF SVM", "Gaussian Process",
		 "Decision Tree", "Random Forest", "Neural Net", "AdaBoost",
		 "Naive Bayes", "QDA"]



labels = pickle.load(open('lyrics_genres.pkl', 'rb'))
features = list(np.load('features.npy'))
partitions = 4

def train_test(i,partitions,features,labels):
	features_train, labels_train, features_test, labels_test = split_data(i, partitions, features, labels)
	clf.fit(features_train, labels_train)
	score = clf.score(features_test, labels_test)
	print(i, ': ',end=' ')
	print(score)

for name, clf in zip(names, classifiers):
	print(name)
	Parallel(n_jobs=num_cores)(delayed(train_test)(i,partitions,features,labels) for i in range(partitions))
	# for i in range(partitions):
	# 	features_train, labels_train, features_test, labels_test = split_data(i, partitions, features, labels)
	# 	clf.fit(features_train, labels_train)
	# 	score = clf.score(features_test, labels_test)
	# 	print(score)







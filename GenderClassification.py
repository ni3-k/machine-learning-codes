""" Using machine learning models to classify genders based on height, weight and shoesize
as seen on https://www.youtube.com/watch?v=T5pRlIbr6gg """

from sklearn import tree, neighbors, svm, ensemble
from sklearn.metrics import accuracy_score

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'female', 'female', 'female', 'male', 'male', 'male', 'female', 'female', 'female', 'male']

# Creating classifiers
clf_decision = tree.DecisionTreeClassifier()
clf_knn = neighbors.KNeighborsClassifier()
clf_random = ensemble.RandomForestClassifier()
clf_svm = svm.SVC()

# Fitting data to classifiers
clf_decision = clf_decision.fit(X, Y)
clf_knn = clf_knn.fit(X, Y)
clf_random = clf_random.fit(X, Y)
clf_svm = clf_svm.fit(X, Y)

# Test Data
X_test=[[198,92,48],[184,84,44],[183,83,44],[166,47,36],[170,60,38],[172,64,39],[182,80,42],[180,80,43]]
Y_test=['male','male','male','female','female','female','male','male']

# Prediction
predict_decision = clf_decision.predict(X_test)
predict_knn = clf_knn.predict(X_test)
predict_random = clf_random.predict(X_test)
predict_svm = clf_svm.predict(X_test)

# Accuracy Score
score = {'decision' : accuracy_score(Y_test, predict_decision), 'knn' : accuracy_score(Y_test, predict_knn), 'random' : accuracy_score(Y_test, predict_random), 'svm' : accuracy_score(Y_test, predict_svm)}

# Printing out Pridiction
for key in score:
	print('Score for %s: %f' %(key, score[key]))
print('\nBest Score is of ' + max(score, key=score.get))

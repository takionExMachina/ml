import botnet_load_data
import botnet_data_preparation
import pickle
from sklearn.linear_model import *
from sklearn.tree import *
from sklearn.naive_bayes import *
from sklearn.neighbors import *
from keras.models import *
from keras.layers import Dense, Activation
from keras.optimizers import *

f = open('botnet_dataset/flowdata.pickle')

data = pickle.load(f)
x_data = data[0]
y_data = data[1]
x_data_test = data[2]
y_data_test = data[3]

botnet_data_preparation.prepare(x_data, y_data, x_data_test, y_data_test)

clf = DecisionTreeClassifier()
clf.fit(x_data, y_data)
prediction = clf.predict(x_data_test)
score = clf.score(x_data_test, y_data_test)
print("Decision Tree Classifier score: ", score*100)

clf = LogisticRegression(C=10000)
clf.fit(x_data, y_data)
prediction = clf.predict(x_data_test)
score = clf.score(x_data_test, y_data_test)
print("Logistic Regression Classifier score: ", score*100)

clf = GaussianNB()
clf.fit(x_data, y_data)
prediction = clf.predict(x_data_test)
score = clf.score(x_data_test, y_data_test)
print("Gaussian Naive Bayes Classifier score: ", score*100)

clf = KNeighborsClassifier()
clf.fit(x_data, y_data)
prediction = clf.predict(x_data_test)
score = clf.score(x_data_test, y_data_test)
print("K-Nearest Neighbors Classifier: ", score*100)

model = Sequential()
model.add(Dense(10, input_dim=9, activation="sigmoid"))
model.add(Dense(10, activation="sigmoid"))
model.add(Dense(1))
sgd = SGD(lr=0.01, decay=0.000001, momentum=0.9, nesterov=True)
model.compile(optimizer=sgd, loss="mse")
model.fit(x_data, y_data, nb_epochs=200, batch_size=100)
score = model.evaluate(x_data_test, y_data_test, verbose=0)
print("Neural Network score: ", score*100)

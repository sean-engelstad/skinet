#first neural network with keras tutorial
#https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

#load the dataset
dataset = loadtxt('pima-indians-diabetes.data.csv', delimiter=',')
#split into input (X) and output (y) variables
X = dataset[:,0:8]
y = dataset[:,8]

#define the keras model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

#compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#fit the keras model on the dataset
model.fit(X, y, epochs=150, batch_size=10)

#evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %0.2f' % (accuracy*100))

#make predictions from the model
predictions = model.predict(X)
#round predictions
rounded = [round(x[0]) for x in predictions]

#make class predictions with the model
predictions = (model.predict(X) > 0.5).astype(int)
#summarize the first 5 classes
for i in range(5):
    print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))

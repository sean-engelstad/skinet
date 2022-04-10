#simple neural net example
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

#load the dataset
dataset = loadtxt('ball.csv', delimiter=',')
#split into input (X) and output (y) variables
X = dataset[:,0:3]
y = dataset[:,3]

#define the keras model
model = Sequential()
model.add(Dense(12, input_dim=3, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

#compile the keras model
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

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
for i in range(3):
    print(X[i])
    print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))

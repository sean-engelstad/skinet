#simple neural net example
from numpy import loadtxt
import numpy as np 
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import cross_val_score
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

#load the dataset
dataset = loadtxt('powers.csv', delimiter=',')
#split into input (X) and output (y) variables
X = dataset[:,0:10]
y = dataset[:,10]

#define the keras model
def baseline_model():

    model = Sequential()
    model.add(Dense(15, input_dim=10, activation='relu'))
    model.add(Dense(15, activation='relu'))
    model.add(Dense(15, activation='relu'))
    model.add(Dense(1, activation='relu'))

    #compile the keras model
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

#fit the keras model on the dataset
estimators = []
estimators.append(('standardize', StandardScaler()))
estimators.append(('mlp', KerasRegressor(build_fn=baseline_model, epochs=50, batch_size=5, verbose=0)))

#build pipeline
pipeline = Pipeline(estimators)
kfold = KFold(n_splits=10)
results = cross_val_score(pipeline, X, y, cv=kfold)
print("Baseline: %.2f (%.2f) MSE" % (results.mean(), results.std()))

#predictions with pipeline
pipeline.fit(X, y)
yhat = pipeline.predict(X)
resid = y - yhat
perResid = abs(resid)/abs(y) * 100
#print(perResid)

#save the pipeline in a .npy file
#np.save("pipeline.npy", pipeline, allow_pickle=True)

#test predictions
import random

for foo in range(30):
    power = random.random()
    x = np.zeros((10))
    for i in range(10):
        number = (i+1)/10
        x[i] = number ** power

    #reshape for single sample
    x = x.reshape(1, -1)
    powerPred = pipeline.predict(x)

    print("power {:.2f}, pred {:.2f}".format(power, powerPred))
    #print(x)
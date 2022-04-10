#predictions with regression pipeline model
import numpy as np
import random
from sklearn.pipeline import Pipeline

data = np.load("pipeline.npy", allow_pickle=True)

#powers example
power = random.random()

x = np.zeros((10))
for i in range(10):
    number = (i+1)/10
    x[i] = number ** power

powerPred = pipeline.predict(x)

print("power %0.3f".format(power)); print(x)
print("predicted power %0.3f".format(powerPred))
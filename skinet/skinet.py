#skinet main class for neural network functions
import numpy as np
class neuralNet():
    def __init__(self, nin, nout):
        self.nin = nin
        self.nout = nout
        self.layers = []

    def addLayer(self, nneurons, style):
        #dimension of input and output to layer
        if (len(self.layers) == 0):
            numin = self.nin
        else:
            numin = self.layers[-1]["nin"]
        numout = nneurons

        weights = np.zeros((numin, numout))
        bias = np.zeros((numout))
        layerDict = {"nin" : numin,
                    "nout" : numout,
                    "weights" : weights,
                    "bias" : bias,
                    "style" : style}
        self.layers.append(layerDict)

    def ReLu(self, x):
        #element-wise Relu, or rectified linear unit
        #for activation of neurons
        out = np.zeros((len(x)))
        for i in range(len(x)):
            if (x[i] > 0):
                out[i] = x[i]
        #otherwise stays 0
        return out

    def dReLu(self, x):
        #derivative of element-wise Relu
        dout = np.zeros((len(x)))
        for i in range(len(x)):
            if (x[i] > 0): dout[i] = 1
        return dout
    
    def regLayer(self, vecin, weights, bias):
        r,c = weights.shape
        vecout = np.zeros((c))

        for i in range(c):
            for j in range(r):
                vecout[i] = weights[j,i] * vecin[j] + bias[i]

        return vecout

    def reluLayer(self, vecin, weights, bias):
        #relu layer aka perceptron
        vecout = self.regLayer(vecin, weights, bias)
        vecout = self.ReLu(vecout)
        return vecout
    
    def updateWeights(self, weightvec):
        temp = list(weightvec)
        for layer in self.layers:
            nin = layer["nin"]
            nout = layer["nout"]
            nweights = nin * nout
            wtemp = temp[0:nweights+1]
            wtemp = wtemp.reshape((nin, nout))
            layer["weights"] = wtemp
            temp[0:nweights+1] = []
        

    def obj(self, x, weights):
        self.updateWeights(weights)
        for layer in self.layers:
            style = layer["style"]
            if (style == "reg"):
                x = self.regLayer(x, layer["weights"], layer["bias"])
            elif (style == "relu"):
                x = self.reluLayer(x, layer["weights"], layer["bias"])
        return x

    def grad(self, x, weights):
        self.updateWeights(weights)
        #compute gradient w.r.t. weights at input x
        gradVec = []
        revlayers = self.layers.reverse()
        for layer in self.layers:
            
        pass

    
    
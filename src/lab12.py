"""Lab 12 starter code: deep NN building blocks + a deep model."""
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def relu(z):
    raise NotImplementedError('TODO: implement this')

def relu_grad(z):
    raise NotImplementedError('TODO: implement this')

def dropout_forward(a, p, rng):
    """Inverted dropout with drop probability p. Return (output, mask)."""
    raise NotImplementedError('TODO: implement this')

def batchnorm_forward(x, gamma, beta, eps=1e-05):
    raise NotImplementedError('TODO: implement this')

def train_deep_model(X, y, seed=0):
    """A deep (>= 3 hidden layers) ReLU network with L2 regularisation. Return fitted model."""
    raise NotImplementedError('TODO: implement this')

def compare_architectures(X, y, seed=0):
    """Train at least three architectures and return {name: test_accuracy}.
Required keys: 'shallow' (1 small layer), 'deep' (3+ layers), 'deep_regularised' (3+ layers, strong L2)."""
    raise NotImplementedError('TODO: implement this')

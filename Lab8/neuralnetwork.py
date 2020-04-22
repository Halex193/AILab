from Lab8.table import attributeNumber, classIndex
import numpy as np


# Linear activation
def activation_function_derivative(x):
    return 1


def activation_function(x):
    return x


class NeuralNetwork:

    def __init__(self, table, learningRate, hiddenNeurons):
        self.data = table
        self.learningRate = learningRate
        self.input = np.array([row[:attributeNumber - 1] for row in table])
        self.weights1 = np.random.rand(self.input.shape[1], hiddenNeurons)
        self.weights2 = np.random.rand(hiddenNeurons, 1)
        self.y = np.array([[row[classIndex] for row in table]]).T
        self.output = np.zeros(self.y.shape)
        self.loss = []
        self.maxDifference = 0
        self.layer1 = None

    def feed_forward(self):
        self.layer1 = activation_function(np.dot(self.input, self.weights1))
        self.output = activation_function(np.dot(self.layer1, self.weights2))

    def back_propagation(self):
        multiplier = 2 / len(self.data)

        difference = (self.y - self.output)

        delta_2 = multiplier * difference

        delta_weights2 = np.dot(self.layer1.T, delta_2) * activation_function_derivative(self.output)

        delta_1 = np.dot(delta_2, self.weights2.T) * activation_function_derivative(self.output)

        delta_weights1 = np.dot(self.input.T, delta_1) * activation_function_derivative(self.layer1)

        self.weights1 += self.learningRate * delta_weights1
        self.weights2 += self.learningRate * delta_weights2

        self.maxDifference = max(difference)[0]

        self.loss.append(sum(difference ** 2))

    def train(self) -> float:
        self.maxDifference = 0
        self.feed_forward()
        self.back_propagation()
        return self.maxDifference

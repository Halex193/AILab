from random import uniform

from Lab7.table import attributeNumber, classIndex


class Neuron:

    def __init__(self, table, learningRate):
        self.data = table
        self.learningRate = learningRate
        self.weight = [uniform(0, 1) for i in range(attributeNumber)]

    def train(self) -> float:
        highestError = 0
        weightDifference = [0] * attributeNumber
        for row in self.data:
            output = self.computeOutput(row)
            error = row[classIndex] - output
            errorPercent = abs(error) / abs(output)
            for i in range(attributeNumber):
                weightDifference[i] += self.learningRate * error * row[i]

            if errorPercent > highestError:
                highestError = errorPercent
        for i in range(attributeNumber):
            self.weight[i] += weightDifference[i]
        return highestError

    def computeOutput(self, row) -> float:
        weightedSum = 0
        for i in range(attributeNumber):
            weightedSum += self.weight[i] * row[i]
        return weightedSum

    def derivative(self, t, o, w):
        return (t - o) * w

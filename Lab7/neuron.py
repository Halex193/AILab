from Lab7.table import attributeNumber, classIndex
from random import uniform


class Neuron:

    def __init__(self, table, learningRate):
        self.data = table
        self.learningRate = learningRate
        self.beta = [0] * (attributeNumber + 1)

    def train(self) -> str:
        N = len(self.data)
        gradient = [0] * (attributeNumber + 1)
        totalError = 0
        for row in self.data:
            output = self.computeOutput(row)
            error = row[classIndex] - output
            totalError += error
            for i in range(attributeNumber):
                gradient[i] += -(2 / N) * error * row[i]
            gradient[attributeNumber] += -(2 / N) * error
        for i in range(attributeNumber):
            self.beta[i] -= self.learningRate * gradient[i]
        self.beta[attributeNumber] -= self.learningRate * gradient[attributeNumber]
        if totalError == 0:
            return "no error | f(x) = " + self.functionStr()
        return "error=" + "{:.2f}".format(totalError / float(len(self.data))) + " | f(x) = " + self.functionStr()

    def computeOutput(self, row) -> float:
        result = self.beta[attributeNumber]
        for i in range(attributeNumber):
            result += self.beta[i] * row[i]
        return result

    def functionStr(self):
        strings = ["{:.2f}".format(self.beta[attributeNumber])]
        for i in range(attributeNumber):
            strings.append("{:.2f}".format(self.beta[i]) + "*x" + str(i+1))
        return " + ".join(strings)

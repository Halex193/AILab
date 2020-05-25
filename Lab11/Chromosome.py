from math import sin, cos
from random import randint, random

MAX_DEPTH = 5
problemTerminalNumber = 24
constantTerminals = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
functions = ['+', '-', '*', 'sin', 'cos']
functionImplementations = {
    '+': lambda child1, child2: child1 + child2,
    '-': lambda child1, child2: child1 - child2,
    '*': lambda child1, child2: child1 * child2,
    'sin': lambda child1, child2: sin(child1),
    'cos': lambda child1, child2: cos(child1)
}
functionNumber = 5
outputClasses = {
    'Slight-Left-Turn': 0,
    'Move-Forward': 1,
    'Slight-Right-Turn': 2,
    'Sharp-Right-Turn': 3

}
outputClassesList = [
    'Slight-Left-Turn',
    'Move-Forward',
    'Slight-Right-Turn',
    'Sharp-Right-Turn'
]

class Chromosome:
    def __init__(self, depth=MAX_DEPTH):
        self.depth = depth
        self.representation = [0 for i in range(2 ** (self.depth + 1) - 1)]
        self.fitness = 0
        self.size = 0

    def growExpression(self, position=0, depth=0):
        if ((position == 0) or (depth < self.depth)) and random() < 0.5:
            self.representation[position] = -randint(1, functionNumber)
            firstChildEnd = self.growExpression(position + 1, depth + 1)
            secondChildEnd = self.growExpression(firstChildEnd, depth + 1)
            return secondChildEnd
        else:
            self.representation[position] = randint(1, problemTerminalNumber + len(constantTerminals))
            self.size = position + 1
            return position + 1

    def evaluateExpression(self, position, trainData):
        node = self.representation[position]
        if node > 0:  # a terminal
            if node <= problemTerminalNumber:
                return trainData[node - 1], position
            else:
                return constantTerminals[node - problemTerminalNumber - 1], position
        elif node < 0:  # a function
            function = functions[-node - 1]
            firstChild = self.evaluateExpression(position + 1, trainData)
            secondChild = self.evaluateExpression(firstChild[1] + 1, trainData)
            return functionImplementations[function](firstChild[0], secondChild[0]), secondChild[1]

    def computeFitness(self, trainData, output):
        error = 0.0
        for i in range(len(trainData)):
            error += abs(outputClasses[output[i]] - self.evaluateExpression(0, trainData[i])[0])
        self.fitness = error

    def traverse(self, position):
        if self.representation[position] > 0:  # terminal
            return position + 1
        else:
            return self.traverse(self.traverse(position + 1))


def crossover(parent1, parent2):
    child = Chromosome()
    while True:
        startParent1 = randint(0, parent1.size - 1)
        endParent1 = parent1.traverse(startParent1)
        startParent2 = randint(0, parent2.size - 1)
        endParent2 = parent2.traverse(startParent2)
        if len(child.representation) > endParent1 + (endParent2 - startParent2 - 1) + (parent1.size - endParent1 - 1):
            break
    i = -1
    for i in range(startParent1):
        child.representation[i] = parent1.representation[i]
    for j in range(startParent2, endParent2):
        i = i + 1
        child.representation[i] = parent2.representation[j]
    for j in range(endParent1, parent1.size):
        i = i + 1
        child.representation[i] = parent1.representation[j]
    child.size = i + 1
    return child


def mutation(chromosome):
    result = Chromosome()
    position = randint(0, chromosome.size - 1)
    result.representation = chromosome.representation[:]
    result.size = chromosome.size
    if result.representation[position] > 0:  # terminal
        result.representation[position] = randint(1, problemTerminalNumber + len(constantTerminals))
    else:  # function
        result.representation[position] = -randint(1, functionNumber)
    return result

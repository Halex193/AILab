from copy import deepcopy
from random import shuffle
from random import randint
from random import random

from PyQt5.QtCore import QThread, pyqtSignal

from Lab3.simulations.pso.individual import Individual


class PSOSimulation(QThread):
    progress = pyqtSignal(int, float, str)

    def __init__(self, n, populationNumber, inertia, cognitive, social, generations, parent=None):
        super(PSOSimulation, self).__init__(parent)
        self.n = n
        self.inertia = inertia
        self.cognitive = cognitive
        self.social = social
        self.maxFitness = self.calculateMaxFitness()
        self.populationNumber = populationNumber
        self.population = self.randomPopulation(populationNumber)
        self.generations = generations
        self.best = max([(x, x.fitness(self.maxFitness)) for x in self.population], key=lambda x: x[1])
        self.generationBest = deepcopy(self.best[0].board)

    def calculateMaxFitness(self):
        board = []
        for i in range(self.n):
            board.append([(1, 1)] * self.n)
        return Individual(self.n, board, board, 1).penalty()

    def initialVelocity(self):
        board = []
        for i in range(self.n):
            column = []
            for j in range(self.n):
                column.append((randint(-2, 2), randint(-2, 2)))
            board.append(column)
        return board

    def randomIndividual(self):
        board = []
        for i in range(self.n):
            column = []
            for j in range(self.n):
                column.append((randint(1, self.n), randint(1, self.n)))
            board.append(column)
        return Individual(self.n, board, self.initialVelocity(), self.maxFitness)

    def randomPopulation(self, number):
        return [self.randomIndividual() for x in range(number)]

    def nextGeneration(self):
        fitnessList =[]
        for i in range(self.populationNumber):
            self.population[i].move(self.inertia, self.cognitive, self.social, self.generationBest, self.maxFitness)
            if self.particleStopped(self.population[i]):
                self.population[i] = self.randomIndividual()
            fitnessList.append((self.population[i].board, self.population[i].fitness(self.maxFitness)))
        generationBest = max(fitnessList, key=lambda x: x[1])
        if generationBest[1] > self.best[1]:
            self.best = (Individual(self.n, deepcopy(generationBest[0]), self.initialVelocity(), self.maxFitness), generationBest[1])
        self.generationBest = deepcopy(generationBest[0])

    def run(self):
        generation = 0
        while not self.isInterruptionRequested() and generation < self.generations:
            generation += 1
            self.progress.emit(generation, self.best[1], str(self.best[0]))
            if self.best[1] == 1:
                self.requestInterruption()
                break
            self.nextGeneration()

    def particleStopped(self, particle):
        if particle.fitness(self.maxFitness) != 1:
            return False
        for i in range(self.n):
            for j in range(self.n):
                if particle.velocity[i][j] >= 1 or particle.velocity[i][j] <= -1:
                    return False
        return True

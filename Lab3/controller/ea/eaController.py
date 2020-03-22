from random import shuffle
from random import randint
from random import random

from PyQt5.QtCore import QThread, pyqtSignal

from Lab3.controller.ea.individual import Individual


class EAController(QThread):
    progress = pyqtSignal(int, float, str)

    def __init__(self, n, populationNumber, mutationChance, generations, parent=None):
        super(EAController, self).__init__(parent)
        self.n = n
        self.mutationChance = mutationChance
        self.maxFitness = self.calculateMaxFitness()
        self.populationNumber = populationNumber
        self.population = self.randomPopulation(populationNumber)
        self.generations = generations
        self.best = max([(x, x.fitness(self.maxFitness)) for x in self.population], key=lambda x: x[1])

    def calculateMaxFitness(self):
        permutation = [1] * self.n
        chromosome = [permutation] * (self.n * 2)
        return Individual(self.n, chromosome).penalty()

    def randomPermutation(self):
        permutation = [x for x in range(1, self.n + 1)]
        shuffle(permutation)
        return permutation

    def randomIndividual(self):
        chromosome = [self.randomPermutation() for x in range(self.n * 2)]
        return Individual(self.n, chromosome)

    def randomPopulation(self, number):
        return [self.randomIndividual() for x in range(number)]

    def crossover(self, individual1: Individual, individual2: Individual):
        childChromosome = []
        for i in range(self.n * 2):
            if randint(1, 2) == 1:
                childChromosome.append(individual1.chromosome[i])
            else:
                childChromosome.append(individual2.chromosome[i])
        return Individual(self.n, childChromosome)

    def mutation(self, individual, chance):
        for i in range(self.n * 2):
            if random() < chance:
                individual.chromosome[i] = self.randomPermutation()
        return individual

    def nextGeneration(self):
        for i in range(self.populationNumber * 5):
            index1 = randint(0, self.populationNumber - 1)
            index2 = randint(0, self.populationNumber - 1)
            if index1 == index2:
                continue

            individual1 = self.population[index1]
            individual2 = self.population[index2]

            child = self.crossover(individual1, individual2)
            child = self.mutation(child, self.mutationChance)

            fitness1 = individual1.fitness(self.maxFitness)
            fitness2 = individual2.fitness(self.maxFitness)
            childFitness = child.fitness(self.maxFitness)

            if fitness1 < fitness2 and fitness1 < childFitness:
                self.population[index1] = child
            elif fitness2 < fitness1 and fitness2 < childFitness:
                self.population[index2] = child

            if childFitness > self.best[1]:
                self.best = (child, childFitness)

    def run(self):
        generation = 0
        while not self.isInterruptionRequested() and generation < self.generations:
            generation += 1
            self.progress.emit(generation, self.best[1], str(self.best[0]))
            if self.best[1] == 1:
                self.requestInterruption()
                break
            self.nextGeneration()
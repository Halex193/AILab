import string
from random import random, choice

from Lab11.Chromosome import Chromosome, mutation, crossover, outputClassesList


class Population:
    def __init__(self, trainingData, output, populationSize=100):
        self.trainingData = trainingData
        self.output = output
        self.population = [Chromosome() for i in range(populationSize)]
        self.populationSize = populationSize
        for chromosome in self.population:
            chromosome.growExpression()

    def train(self) -> float:
        newChromosomes = []
        for i in range(self.populationSize):
            if random() < 0.5:
                newChromosomes.append(mutation(choice(self.population)))
            else:
                newChromosomes.append(crossover(choice(self.population), choice(self.population)))
        self.population += newChromosomes

        for chromosome in self.population:
            chromosome.computeFitness(self.trainingData, self.output)

        fitnessEvaluation = [(chromosome, chromosome.fitness) for chromosome in self.population]
        fitnessEvaluation = sorted(fitnessEvaluation, key=lambda x: x[1])
        self.population = [x[0] for x in fitnessEvaluation[:self.populationSize]]
        return fitnessEvaluation[0][1] / len(self.trainingData)

    def predict(self, inputData) -> string:
        fitnessEvaluation = [(chromosome, chromosome.fitness) for chromosome in self.population]
        fitnessEvaluation = sorted(fitnessEvaluation, key=lambda x: x[1])
        bestChromosome = fitnessEvaluation[0][0]
        output = int(bestChromosome.evaluateExpression(0, inputData)[0])
        if output > 3:
            return 'No class chosen'
        return outputClassesList[output]

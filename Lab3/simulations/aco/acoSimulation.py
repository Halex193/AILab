import itertools

from PyQt5.QtCore import QThread, pyqtSignal

from Lab3.simulations.aco.ant import Ant


class ACOSimulation(QThread):
    progress = pyqtSignal(int, float, str)

    def __init__(self, n, populationNumber, alpha, beta, q0, rho, generations, parent=None):
        super(ACOSimulation, self).__init__(parent)
        self.n = n
        self.populationNumber = populationNumber
        self.alpha = alpha
        self.beta = beta
        self.q0 = q0
        self.rho = rho
        self.generations = generations
        self.permutations = [list(x) for x in itertools.permutations([i for i in range(1, self.n + 1)])]
        self.trace = [[1 for i in range(len(self.permutations))] for j in range(len(self.permutations))]
        self.best = (0, 0)
        self.maxFitness = self.calculateMaxFitness()

    def nextGeneration(self):
        antSet = [Ant(self.n, self.permutations) for i in range(self.populationNumber)]
        for i in range(self.n * 2):
            for x in antSet:
                x.makeMove(self.q0, self.trace, self.alpha, self.beta, self.maxFitness)
        dTrace = [1.0 / antSet[i].fitness(self.maxFitness) for i in range(len(antSet))]
        for i in range(len(self.permutations)):
            for j in range(len(self.permutations)):
                self.trace[i][j] = (1 - self.rho) * self.trace[i][j]
        for i in range(len(antSet)):
            for j in range(len(antSet[i].path) - 1):
                x = antSet[i].path[j]
                y = antSet[i].path[j + 1]
                self.trace[x][y] = self.trace[x][y] + dTrace[i]
        f = [[antSet[i].fitness(self.maxFitness), i] for i in range(len(antSet))]
        f = max(f)
        if f[0] > self.best[1]:
            self.best = (antSet[f[1]], f[0])

    def calculateMaxFitness(self):
        permutation = [1] * self.n
        permutationPath = [permutation] * (self.n * 2)
        return Ant(self.n, self.permutations).penalty(permutationPath)

    def run(self):
        generation = 0
        while not self.isInterruptionRequested() and generation < self.generations:
            generation += 1
            self.progress.emit(generation, self.best[1], str(self.best[0]))
            if self.best[1] == 1:
                self.requestInterruption()
                break
            self.nextGeneration()

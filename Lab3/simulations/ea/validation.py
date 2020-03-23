from PyQt5.QtCore import QThread, pyqtSignal
from numpy import mean
from numpy import std

from Lab3.simulations.ea.eaSimulation import EASimulation


class Validation(QThread):
    done = pyqtSignal(float, float, list)
    runs = 30
    populationSize = 40
    mutationChance = 0.2
    boardSize = 4
    generations = 1000

    def __init__(self, parent=None):
        super(Validation, self).__init__(parent)
        self.graph = []

    def run(self) -> None:
        simulations = [EASimulation(self.boardSize, self.populationSize, self.mutationChance, self.generations)
                       for i in range(self.runs)]

        self.graph.append(mean(self.gatherFitness(simulations)))
        for i in range(self.generations):
            if self.isInterruptionRequested():
                return
            for simulation in simulations:
                simulation.nextGeneration()
            self.graph.append(mean(self.gatherFitness(simulations)))
        fitness = self.gatherFitness(simulations)
        m = mean(fitness)
        s = std(fitness)
        self.done.emit(m, s, self.graph)

    def gatherFitness(self, simulations):
        fitness = []
        for simulation in simulations:
            fitness.append(simulation.best[1])
        return fitness

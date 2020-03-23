from PyQt5.QtCore import QThread, pyqtSignal
from numpy import mean
from numpy import std
from Lab3.controller.ea.eaSimulation import EASimulation


class Validation(QThread):
    done = pyqtSignal(float, float, list)
    runs = 30
    populationSize = 40
    mutationChance = 0.2
    boardSize = 4
    generations = 1000

    def __init__(self, parent=None):
        super(Validation, self).__init__(parent)
        self.fitness = [0] * self.runs
        self.graph = []

    def run(self) -> None:
        simulations = [EASimulation(self.boardSize, self.populationSize, self.mutationChance, self.generations)
                       for i in range(self.runs)]
        for i in range(len(simulations)):
            simulations[i].progress.connect(lambda generation, fitness, board: self.progress(i, generation, fitness))
            simulations[i].start()
        for i in range(len(simulations)):
            simulations[i].wait()
        self.done.emit(mean(self.fitness), std(self.fitness), self.graph)

    def progress(self, population, generation, fitness):
        self.fitness[population] = fitness
        self.graph.append(mean(self.fitness))


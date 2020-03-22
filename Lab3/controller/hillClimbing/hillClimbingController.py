from PyQt5.QtCore import QThread, pyqtSignal
from qtconsole.qt import QtCore

from Lab3.controller.hillClimbing.state import State
from random import randint


class HillClimbingController(QThread):
    progress = pyqtSignal(float, str)

    def __init__(self, n, parent=None):
        super(HillClimbingController, self).__init__(parent)
        self.n = n
        self.maxFitness = self.calculateMaxFitness()
        self.state = self.randomState()

    def calculateMaxFitness(self):
        board = []
        for i in range(self.n):
            board.append([(1, 1)] * self.n)
        return State(self.n, board).penalty()

    def randomState(self):
        board = []
        for i in range(self.n):
            column = []
            for j in range(self.n):
                column.append((randint(1, self.n), randint(1, self.n)))
            board.append(column)
        return State(self.n, board)

    def orderStates(self, states):
        aux = [(x, x.fitness(self.maxFitness)) for x in states]
        aux.sort(key=lambda t: t[1], reverse=True)
        return [x[0] for x in aux]

    def nextGeneration(self):
        states = self.state.adjacentStates()
        candidate = self.orderStates(states)[0]
        if candidate.fitness(self.maxFitness) > self.state.fitness(self.maxFitness):
            self.state = candidate
        else:
            self.requestInterruption()

    def run(self):
        while not self.isInterruptionRequested():
            self.progress.emit(self.state.fitness(self.maxFitness), str(self.state))
            self.nextGeneration()


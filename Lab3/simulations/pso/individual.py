from copy import deepcopy
from random import random


class Individual:
    def __init__(self, n, board, velocity, maxFitness):
        self.n = n
        self.board = board
        self.velocity = velocity
        self.best = (board, self.fitness(maxFitness))

    def fitness(self, maxFitness):
        fitness = maxFitness
        fitness -= self.penalty()
        return fitness / maxFitness

    def penalty(self):
        penalty = 0
        for i in range(self.n):
            penalty += self.checkLine(i, 0)
            penalty += self.checkLine(i, 1)
        for j in range(self.n):
            penalty += self.checkColumn(j, 0)
            penalty += self.checkColumn(j, 1)
        penalty += self.checkCells()
        return penalty

    def checkColumn(self, j, dimension):
        penalty = 0
        numbers = {}
        for i in range(self.n):
            number = self.board[i][j][dimension]
            if number not in numbers:
                numbers[number] = 0
            else:
                penalty += 1
        return penalty

    def checkLine(self, i, dimension):
        penalty = 0
        numbers = {}
        for j in range(self.n):
            number = self.board[i][j][dimension]
            if number not in numbers:
                numbers[number] = 0
            else:
                penalty += 1
        return penalty

    def checkCells(self):
        penalty = 0
        pairs = {}
        for i in range(self.n):
            for j in range(self.n):
                pair = self.board[i][j]
                if pair not in pairs:
                    pairs[pair] = 0
                else:
                    penalty += 1
        return penalty

    def __str__(self):
        string = ""
        for i in range(self.n):
            for j in range(self.n):
                string += str(self.board[i][j]) + " "
            string += "\n"
        return string

    def move(self, inertia, cognitive, social, bestNeighbour, maxFitness):
        self.changeVelocity(inertia, cognitive, social, bestNeighbour)
        self.changePosition(maxFitness)

    def changeVelocity(self, inertia, cognitive, social, bestNeighbour):
        for i in range(self.n):
            for j in range(self.n):
                self.velocity[i][j] = (
                    self.velocity[i][j][0] * inertia +
                    cognitive * random() * (self.best[0][i][j][0] - self.board[i][j][0]) +
                    social * random() * (bestNeighbour[i][j][0] - self.board[i][j][0]),

                    self.velocity[i][j][1] * inertia +
                    cognitive * random() * (self.best[0][i][j][1] - self.board[i][j][1]) +
                    social * random() * (bestNeighbour[i][j][1] - self.board[i][j][1])
                )

    def changePosition(self, maxFitness):
        for i in range(self.n):
            for j in range(self.n):
                self.board[i][j] = (
                    self.addVelocity(self.board[i][j][0], self.velocity[i][j][0]),
                    self.addVelocity(self.board[i][j][1], self.velocity[i][j][1])
                )
        fitness = self.fitness(maxFitness)
        if fitness > self.best[1]:
            self.best = (deepcopy(self.board), fitness)

    def addVelocity(self, position, velocity):
        newPosition = position + velocity
        if newPosition < 1:
            return 1

        if newPosition > self.n:
            return self.n

        return int(newPosition)

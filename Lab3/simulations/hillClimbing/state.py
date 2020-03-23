from copy import deepcopy


class State:
    def __init__(self, n, board):
        self.n = n
        self.board = board

    def adjacentStates(self):
        states = []
        for i in range(self.n):
            for j in range(self.n):
                pair = self.board[i][j]
                value1 = pair[0]
                if value1 - 1 > 0:
                    newBoard = deepcopy(self.board)
                    newBoard[i][j] = (value1 - 1, pair[1])
                    states.append(State(self.n, newBoard))
                if value1 + 1 <= self.n:
                    newBoard = deepcopy(self.board)
                    newBoard[i][j] = (value1 + 1, pair[1])
                    states.append(State(self.n, newBoard))

                value2 = pair[1]
                if value2 - 1 > 0:
                    newBoard = deepcopy(self.board)
                    newBoard[i][j] = (pair[0], value2 - 1)
                    states.append(State(self.n, newBoard))
                if value2 + 1 <= self.n:
                    newBoard = deepcopy(self.board)
                    newBoard[i][j] = (pair[0], value2 + 1)
                    states.append(State(self.n, newBoard))
        return states

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

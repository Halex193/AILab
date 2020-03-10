from copy import copy, deepcopy

from Lab2.configuration import Configuration
from Lab2.state import State


class Problem:

    def __init__(self):
        self.n = 0

    def setN(self, n):
        self.n = n

    def expandState(self, state: State):
        configuration = state.lastConfiguration()
        if len(configuration.queens) >= self.n:
            return []

        newStates = []
        for i in range(self.n):
            for j in range(self.n):
                if (i, j) not in configuration.queens:
                    newConfiguration = deepcopy(configuration)
                    newConfiguration = newConfiguration + (i, j)
                    newStates.append(copy(state) + newConfiguration)
        return newStates

    def heuristic(self, state):
        score = 0
        queens = state.lastConfiguration().queens
        for i in range(self.n):
            count = 0
            for queen in queens:
                if queen[0] == i:
                    count += 1
            if count != 1:
                score += 1
        for j in range(self.n):
            count = 0
            for queen in queens:
                if queen[1] == j:
                    count += 1
            if count != 1:
                score += 1
        for i in range(len(queens)):
            for j in range(i + 1, len(queens)):
                if abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                    score += 1
        return score

    def checkFinalState(self, state):
        queens = state.lastConfiguration().queens
        if len(queens) != self.n:
            return False
        for i in range(self.n):
            count = 0
            for queen in queens:
                if queen[0] == i:
                    count += 1
            if count != 1:
                return False
        for j in range(self.n):
            count = 0
            for queen in queens:
                if queen[1] == j:
                    count += 1
            if count != 1:
                return False
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                    return False
        return True

    def initialState(self):
        return State() + Configuration(self.n)

from copy import copy, deepcopy

from Lab2.state import State


class Problem:

    def __init__(self):
        self.n = 0

    def setN(self, n):
        self.n = n

    def expandState(self, state):
        board = state.lastBoard()
        newStates = []
        for i in range(self.n):
            for j in range(self.n):
                if board[i][j] == 0:
                    newBoard = deepcopy(board)
                    newBoard[i][j] = 1
                    newStates.append(copy(state) + newBoard)
        return newStates

    def heuristic(self, state):
        score = 0
        board = state.lastBoard()
        for i in range(self.n):
            count = 0
            for j in range(self.n):
                count += board[i][j]
            if count != 1:
                score += 1
        for j in range(self.n):
            count = 0
            for i in range(self.n):
                count += board[i][j]
            if count != 1:
                score += 1
        ones = []
        for i in range(self.n):
            for j in range(self.n):
                if board[i][j] == 1:
                    ones.append((i, j))
        for i in range(len(ones)):
            for j in range(i + 1, len(ones)):
                if abs(ones[i][0] - ones[j][0]) == abs(ones[i][1] - ones[j][1]):
                    score += 1
        return score

    def checkFinalState(self, state):
        board = state.lastBoard()
        for i in range(self.n):
            count = 0
            for j in range(self.n):
                count += board[i][j]
            if count != 1:
                return False
        for j in range(self.n):
            count = 0
            for i in range(self.n):
                count += board[i][j]
            if count != 1:
                return False
        ones = []
        for i in range(self.n):
            for j in range(self.n):
                if board[i][j] == 1:
                    ones.append((i, j))
        for i in range(len(ones)):
            for j in range(i + 1, len(ones)):
                if abs(ones[i][0] - ones[j][0]) == abs(ones[i][1] - ones[j][1]):
                    return False
        return True

    def initialState(self):
        board = []
        for i in range(self.n):
            board.append([0] * self.n)
        return State() + board

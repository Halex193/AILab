import copy
from math import sqrt

from numpy.random import randint


def solution(board, size, intendedSum):
    for row in board:
        if sum(row) != intendedSum:
            return False
    for j in range(size):
        colSum = 0
        for i in range(size):
            colSum += board[i][j]
        if colSum != intendedSum:
            return False

    squareSize = int(sqrt(size))
    for s in range(squareSize):
        for t in range(squareSize):
            squareSum = 0
            for i in range(squareSize):
                for j in range(squareSize):
                    squareSum += board[s * squareSize + i][t * squareSize + j]
            if squareSum != intendedSum:
                return False
    return True


def main():
    with open('sudoku.txt', 'r') as f:
        board = [[int(num) for num in line.split(' ')] for line in f]
        size = len(board)
        print("Board:")
        printBoard(board)

        intendedSum = size * (size + 1) / 2
        chances = int(input("chances: "))
        print("Computing...")
        for k in range(chances):
            newBoard = copy.deepcopy(board)
            for i in range(size):
                for j in range(size):
                    if newBoard[i][j] == 0:
                        newBoard[i][j] = randint(1, size + 1)
            if solution(newBoard, size, intendedSum):
                printBoard(newBoard)
                return
        print("No solution found!")


def printBoard(newBoard):
    print('\n'.join([''.join(['{:2}'.format(item) for item in row])
                     for row in newBoard]))


if __name__ == '__main__':
    main()

#  3 4 1 2
#  2 1 4 3
#  1 2 3 4
#  4 3 2 1



from random import sample

from Lab6.fileOperations import readData
from Lab6.table import Table, allAttributes
from Lab6.tree import Tree


def run(testPercent):
    data = readData()
    allRows = [i for i in range(len(data))]
    testRowsNumber = int(testPercent * len(allRows))
    testRows = sample(allRows, testRowsNumber)
    trainingRows = [row for row in allRows if row not in testRows]

    table = Table(data, allAttributes, trainingRows)
    tree = Tree(table)

    successes = 0
    for row in testRows:
        if tree.testRow(data[row]):
            successes += 1
    return successes / testRowsNumber


def test(testPercent):
    runs = 1000
    runResults = [run(testPercent) for i in range(runs)]
    print(str(max(runResults)))


if __name__ == '__main__':
    test(0.1)

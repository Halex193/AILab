from Lab5.fileOperations import readData
from Lab5.table import Table, allAttributes
from Lab5.tree import Tree
from random import sample

testPercent = 0.2


def run():
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

def test():
    runs = 1000
    print("Starting test...")
    print(str(max([run() for i in range(runs)])))

if __name__ == '__main__':
    test()

import csv
import pickle

from Lab11.Chromosome import problemTerminalNumber


def readInput():
    testData = []
    with open('files/input.in') as csv_file:
        for row in csv.reader(csv_file, delimiter=','):
            testData.append([float(row[i]) for i in range(problemTerminalNumber)])
    return testData


def readTrainingData():
    trainingData = []
    output = []
    with open('files/training.in') as csv_file:
        for row in csv.reader(csv_file, delimiter=','):
            trainingData.append([float(row[i]) for i in range(problemTerminalNumber)])
            output.append(row[problemTerminalNumber])
    return trainingData, output


def writeOutput(output):
    with open("files/output.out", "w") as file:
        file.write(output)


def serializePopulation(population):
    with open("files/output.out", "b") as file:
        pickle.dump(population, file)


def deserializePopulation():
    with open("files/population3.bin", "b") as file:
        return pickle.load(file)

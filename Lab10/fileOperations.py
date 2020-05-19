import csv

from Lab10.model.Trapezoid import Trapezoid
from Lab10.model.Triangle import Triangle


def readInput():
    with open('files/input.in') as csv_file:
        return [(int(row[0]), int(row[1])) for row in csv.reader(csv_file, delimiter=' ')]


def readData():
    temperature = {}
    humidity = {}
    time = {}
    table = {}

    with open('files/problem.in') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        line = 1
        for row in csv_reader:
            if line <= 5:
                temperature[row[0]] = parseShape(row)
            elif line <= 8:
                humidity[row[0]] = parseShape(row)
            elif line <= 11:
                time[row[0]] = parseShape(row)
            else:
                if row[0] not in table:
                    table[row[0]] = {}
                table[row[0]][row[1]] = row[2]
            line += 1

    return temperature, humidity, time, table


def parseShape(row):
    if len(row) == 4:
        return Triangle(int(row[1]), int(row[2]), int(row[3]))
    return Trapezoid(int(row[1]), int(row[2]), int(row[3]), int(row[4]))


def writeOutput(output):
    with open("files/output.out", "w") as file:
        file.write(output)

import csv

from Lab6.table import classAttribute, allAttributes


def readData():
    result = []
    with open('balance-scale.data') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            result.append({
                classAttribute: row[0],
                allAttributes[0]: row[1],
                allAttributes[1]: row[2],
                allAttributes[2]: row[3],
                allAttributes[3]: row[4]
            })
    return result

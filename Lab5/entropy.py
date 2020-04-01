from Lab5.table import *
from numpy import log2
import operator


def selectAttribute(table: Table):
    if len(table.attributes) == 1:
        return table.attributes[0]
    ES = entropy(table)
    gains = {}
    for attribute in table.attributes:
        entropySum = 0
        for value in attributeValues:
            partition = table.subset(attribute, value)
            if len(partition) == 0:
                continue
            entropySum += len(partition) / len(table) * entropy(partition)
        gains[attribute] = ES - entropySum
    return max(gains.items(), key=operator.itemgetter(1))[0]


def entropy(table):
    classValueCount = {}
    for row in table:
        if row[classAttribute] not in classValueCount:
            classValueCount[row[classAttribute]] = 1
        else:
            classValueCount[row[classAttribute]] += 1
    tableRows = len(table)
    classValueList = list(classValueCount.values())
    classProportions = map(lambda x: x/tableRows, classValueList)
    return sum(map(lambda x: -x * log2(x), classProportions))

from Lab11.controller import Population
from Lab11.fileOperations import readTrainingData, readInput, writeOutput, serializePopulation, appendStatus

if __name__ == '__main__':
    (trainingData, output) = readTrainingData()
    population = Population(trainingData, output)
    i = 1
    while True:
        error = population.train()
        message = "Epoch {} - {:.3f}".format(i, error)
        print(message)
        appendStatus(message)
        i += 1
        if error < 0.1:
            serializePopulation(population, "1")
            break
        elif error < 0.2:
            serializePopulation(population, "2")
        elif error < 0.3:
            serializePopulation(population, "3")
        elif error < 0.4:
            serializePopulation(population, "4")
        elif error < 0.5:
            serializePopulation(population, "5")
        elif error < 0.6:
            serializePopulation(population, "6")
        elif error < 0.7:
            serializePopulation(population, "7")
    testData = readInput()
    allOutput = []
    for i in range(len(testData)):
        output = population.predict(testData[i])
        print()
        allOutput.append(output)
    writeOutput('\n'.join(allOutput))

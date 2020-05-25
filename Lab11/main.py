from Lab11.controller import Population
from Lab11.fileOperations import readTrainingData, readInput, writeOutput, serializePopulation

if __name__ == '__main__':
    (trainingData, output) = readTrainingData()
    population = Population(trainingData, output)
    epochs = 1000
    for i in range(epochs):
        error = population.train()
        print("Epoch {} - {:.3f}".format(i, error))
        if error < 0.4:
            serializePopulation(population)
            break
    testData = readInput()
    allOutput = []
    for i in range(len(testData)):
        output = population.predict(testData[i])
        print()
        allOutput.append(output)
    writeOutput('\n'.join(allOutput))

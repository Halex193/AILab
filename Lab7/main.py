from Lab7.fileOperations import readData
from Lab7.neuron import Neuron


def run(learningRate, iterations):
    data = readData()
    neuron = Neuron(data, learningRate)

    print('Training started...')
    for i in range(iterations):
        print("Iteration + " + str(i) + " error: " + str(neuron.train()))


if __name__ == '__main__':
    run(0.5, 100)

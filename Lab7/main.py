from Lab7.fileOperations import readData
from Lab7.neuron import Neuron


def run(learningRate, iterations):
    data = readData()
    neuron = Neuron(data, learningRate)

    print('Training started...')
    for i in range(iterations):
        output = neuron.train()
        if i % 100 == 0:
            print("Iteration " + str(i) + ": " + output)


if __name__ == '__main__':
    run(0.0001, 50000)

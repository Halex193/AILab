from Lab8.fileOperations import readData
from Lab8.neuralnetwork import NeuralNetwork
import matplotlib.pyplot as plt


def run(learningRate, iterations):
    data = readData()
    neuralNetwork = NeuralNetwork(data, learningRate, 4)

    print('Training started...')
    for i in range(iterations):
        maxError = neuralNetwork.train()
        if (i + 1) % 100 == 0:
            print("{:5}".format(i + 1) +
                  " - maximum error: " +
                  "{:.5f}".format(maxError) +
                  " - loss : " +
                  "{:.5f}".format(neuralNetwork.loss[i][0])
                  )

    x = [i for i in range(iterations)]
    y = neuralNetwork.loss
    plt.plot(x, y, label='Loss value / iteration')
    plt.xlabel('Iterations')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    run(0.0000001, 10000)

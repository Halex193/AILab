from Lab10.FuzzyProcessor import FuzzyProcessor
from Lab10.fileOperations import readData, readInput, writeOutput

if __name__ == '__main__':
    processor = FuzzyProcessor(readData())
    output = []
    for input in readInput():
        (result, logs) = processor.process(input)
        for log in logs:
            print(log)
        message = "{}°C, {}% -> {} minutes".format(input[0], input[1], result)
        output.append(message)
        print(message)
    writeOutput('\n'.join(output))

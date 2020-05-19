class FuzzyProcessor:
    def __init__(self, data):
        (self.temperature, self.humidity, self.time, self.table) = data

    def process(self, input):
        logs = []
        (input_temperature, input_humidity) = input
        # logs.append("Input: temperature {}°C, humidity {}%".format(input_temperature, input_humidity))

        temperature_probability = {temperature: shape.membership(input_temperature)
                                   for (temperature, shape) in self.temperature.items()}
        # logs.append("Probabilities for each temperature class: {}".format(temperature_probability))

        humidity_probability = {humidity: shape.membership(input_humidity)
                                for (humidity, shape) in self.humidity.items()}
        # logs.append("Probabilities for each humidity class: {}".format(humidity_probability))

        time_probability = {time: 0 for time in self.time.keys()}
        for humidity in self.humidity.keys():
            for temperature in self.temperature.keys():
                time = self.table[humidity][temperature]
                probability = min(humidity_probability[humidity], temperature_probability[temperature])
                time_probability[time] = max(probability, time_probability[time])
        # logs.append("Probability for each time class: {}".format(time_probability))

        coaData = [(self.time[time].b, probability) for (time, probability) in time_probability.items()]
        # logs.append("Probability for each temperature: {}".format(coaData))

        coa = sum([time * probability for (time, probability) in coaData]) / \
              sum([probability for (_, probability) in coaData])
        # logs.append("Result: {} minutes".format(coa))
        return coa, logs

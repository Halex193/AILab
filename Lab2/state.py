class State:
    def __init__(self):
        self.configurations = []

    def __add__(self, configuration):
        self.configurations.append(configuration)
        return self

    def __copy__(self):
        state = State()
        state.configurations = self.configurations[:]
        return state

    def __str__(self):
        string = ""
        for configuration in self.configurations:
            string += str(configuration)
            string += "--------------------\n"
        return string

    def lastConfiguration(self):
        return self.configurations[-1]
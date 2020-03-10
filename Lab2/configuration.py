class Configuration:
    def __init__(self, n):
        self.queens = []
        self.n = n

    def __add__(self, queen):
        self.queens.append(queen)
        return self

    def __str__(self):
        string = ""
        for i in range(self.n):
            for j in range(self.n):
                if (i, j) in self.queens:
                    string += "1"
                else:
                    string += "0"
                string += " "
            string += "\n"
        return string

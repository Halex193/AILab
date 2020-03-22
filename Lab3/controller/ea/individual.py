class Individual:
    def __init__(self, n, chromosome):
        self.n = n
        self.chromosome = chromosome

    def fitness(self, maxFitness):
        fitness = maxFitness
        fitness -= self.penalty()
        return fitness / maxFitness

    def penalty(self):
        penalty = 0
        for j in range(self.n):
            penalty += self.checkColumn(j, 0)
            penalty += self.checkColumn(j, 1)
        penalty += self.checkCells()
        return penalty

    def checkColumn(self, j, dimension):
        penalty = 0
        numbers = {}
        for i in range(self.n):
            number = self.chromosome[i + dimension * self.n][j]
            if number not in numbers:
                numbers[number] = 0
            else:
                penalty += 1
        return penalty

    def checkCells(self):
        penalty = 0
        pairs = {}
        for i in range(self.n):
            for j in range(self.n):
                pair = (self.chromosome[i][j], self.chromosome[i + self.n][j])
                if pair not in pairs:
                    pairs[pair] = 0
                else:
                    penalty += 1
        return penalty

    def __str__(self):
        string = ""
        for i in range(self.n):
            for j in range(self.n):
                string += str((self.chromosome[i][j], self.chromosome[i + self.n][j])) + " "
            string += "\n"
        return string

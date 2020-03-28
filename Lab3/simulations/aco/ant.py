from random import randint, random, choice


class Ant:
    def __init__(self, n, permutations):
        self.n = n
        self.permutations = permutations
        self.path = [randint(0, len(self.permutations) - 1)]

    def penalty(self):
        permutationPath = [self.permutations[i] for i in self.path]
        penalty = 0
        for j in range(self.n):
            penalty += self.checkColumn(j, self.n, 0, permutationPath)
            penalty += self.checkColumn(j, self.n, 1, permutationPath)
        penalty += self.checkCells(self.n, permutationPath)
        return penalty

    def checkColumn(self, j, nrRows, dimension, permutationPath):
        penalty = 0
        numbers = {}
        for i in range(nrRows):
            number = permutationPath[i + dimension * self.n][j]
            if number not in numbers:
                numbers[number] = 0
            else:
                penalty += 1
        return penalty

    def checkCells(self, nrRows, permutationPath):
        penalty = 0
        pairs = {}
        for i in range(nrRows):
            for j in range(self.n):
                pair = (permutationPath[i][j], permutationPath[i + self.n][j])
                if pair not in pairs:
                    pairs[pair] = 0
                else:
                    penalty += 1
        return penalty

    def distMove(self, i):
        permutationPath = [self.permutations[i] for i in self.path]
        permutationPath.append(self.permutations[i])

        penalty = 0
        dimension0nrRows = self.n if len(permutationPath) // self.n == 1 else len(permutationPath)
        dimension1nrRows = len(permutationPath) % self.n if len(permutationPath) // self.n == 1 else 0
        for j in range(self.n):
            penalty += self.checkColumn(j, dimension0nrRows, 0, permutationPath)
            penalty += self.checkColumn(j, dimension1nrRows, 1, permutationPath)

        penalty += self.checkCells(dimension1nrRows, permutationPath)
        return penalty

    def nextMoves(self):
        moves = []
        for i in range(self.permutations):
            if i not in self.path:
                moves.append(i)
        return moves

    def addMove(self, q0, trace, alpha, beta):
        p = [self.n ** 2 for i in range(len(self.permutations))]
        nextSteps = self.nextMoves()
        if len(nextSteps) == 0:
            return False
        for i in nextSteps:
            p[i] = self.distMove(i)
            if p[i] < 0:
                raise ArithmeticError()
        p = [(p[i] ** beta) * (trace[self.path[-1]][i] ** alpha) for i in range(len(p))]
        if random() < q0:
            p = [[i, p[i]] for i in range(len(p))]
            p = min(p, key=lambda a: a[1])
            self.path.append(p[0])
        else:
            s = sum(p)
            if s == 0:
                return choice(nextSteps)
            p = [p[i] / s for i in range(len(p))]
            p = [sum(p[0:i + 1]) for i in range(len(p))]
            r = random()
            i = 0
            while r > p[i]:
                i = i + 1
            self.path.append(i)
        return True

    def __str__(self):
        permutationPath = [self.permutations[i] for i in self.path]
        string = ""
        for i in range(self.n):
            for j in range(self.n):
                string += str((permutationPath[i][j], permutationPath[i + self.n][j])) + " "
            string += "\n"
        return string

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def membership(self, x):
        minArguments = [1]
        if self.b != self.a:
            minArguments.append((x - self.a) / (self.b - self.a))
        if self.c != self.b:
            minArguments.append((self.c - x) / (self.c - self.b))
        return max(0, min(minArguments))

    def __repr__(self) -> str:
        return "Triangle(a={}, b={}, c={})".format(self.a, self.b, self.c)


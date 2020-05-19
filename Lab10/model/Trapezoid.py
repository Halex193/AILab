class Trapezoid:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def membership(self, x):
        minArguments = [1]
        if self.b != self.a:
            minArguments.append((x - self.a) / (self.b - self.a))
        if self.d != self.c:
            minArguments.append((self.d - x) / (self.d - self.c))
        return max(0, min(minArguments))

    def __repr__(self) -> str:
        return "Trapezoid(a={}, b={}, c={}, d={})".format(self.a, self.b, self.c, self.d)
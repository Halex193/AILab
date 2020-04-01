from copy import deepcopy

allAttributes = ['LW', 'LD', 'RW', 'RD']
attributeValues = ['1', '2', '3', '4', '5']
classAttribute = 'class'
classValues = ['L', 'B', 'R']


class Table:
    def __init__(self, data, attributes, rows):
        self.data = data
        self.attributes = attributes
        self.rows = rows
        self.current = 0

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current == len(self.rows):
            raise StopIteration
        current = self.current
        self.current += 1
        return self.data[self.rows[current]]

    def __getitem__(self, item):
        return self.data[self.rows[item]]

    def __len__(self):
        return len(self.rows)

    def checkAllClass(self):
        firstClass = self[0][classAttribute]
        for item in self:
            if item[classAttribute] != firstClass:
                return None
        return firstClass

    def getMajorityClass(self):
        classes = {}

        for item in self:
            if item[classAttribute] not in classes:
                classes[item[classAttribute]] = 1
            else:
                classes[item[classAttribute]] += 1

        aux = [(value, classes[value]) for value in classes]
        return max(aux, key=lambda x: x[1])[0]

    def subset(self, separationAttribute, value):
        newRows = []
        for row in self.rows:
            if self.data[row][separationAttribute] == value:
                newRows.append(row)

        remainingAttributes = deepcopy(self.attributes)
        remainingAttributes.remove(separationAttribute)
        return Table(self.data, remainingAttributes, newRows)
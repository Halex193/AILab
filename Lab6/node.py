class Node:
    def __init__(self):
        self.info = None
        self.children = {}
        self.leaf = False

    def addChild(self, child, value):
        self.children[value] = child

    def classNode(self, classValue):
        self.info = classValue
        self.leaf = True

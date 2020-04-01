from Lab5.entropy import selectAttribute
from Lab5.node import Node
from Lab5.table import Table, classAttribute, attributeValues


class Tree:

    def __init__(self, table):
        self.root = self.generate(table)

    def testRow(self, row) -> bool:
        node = self.root
        while not node.leaf:
            value = row[node.info]
            node = node.children[value]
        return node.info == row[classAttribute]

    def generate(self, table: Table) -> Node:
        node = Node()
        allClass = table.checkAllClass()
        if allClass is not None:
            node.classNode(allClass)
            return node
        if len(table.attributes) == 0:
            majorityClass = table.getMajorityClass()
            node.classNode(majorityClass)
            return node
        separationAttribute = selectAttribute(table)
        node.info = separationAttribute
        for value in attributeValues:
            newTable = table.subset(separationAttribute, value)
            if len(newTable) == 0:
                majorityClass = table.getMajorityClass()
                childNode = Node()
                childNode.classNode(majorityClass)
                node.addChild(childNode, value)
            else:
                node.addChild(self.generate(newTable), value)
        return node

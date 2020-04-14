import csv

class Node:
    def __init__(self, name):
        self.name = name
        self.links = []
        self.visited = False
    
class Link:
    def __init__(self, fromNode, toNode, cost):
        self.cost = cost
        self.nodes = [fromNode, toNode]

class Graph:
    def __init__(self, fileName):
        self.nodes = {}
        with open(fileName, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ')
            i = 0
            for row in reader:
                i += 1
                if i == 1:
                    self.V = int(row[0])
                elif i == 2:
                    self.E = int(row[0])

                if len(row) == 2:
                    self.add_edge(int(row[0]), int(row[1]))

    def add_edge(self, fromNodeKey, toNodeKey):
        if not self.nodes.get(fromNodeKey):
            self.nodes[fromNodeKey] = Node(fromNodeKey)
        if not self.nodes.get(toNodeKey):
            self.nodes[toNodeKey] = Node(toNodeKey)

        fromNode = self.nodes[fromNodeKey]
        toNode = self.nodes[toNodeKey]

        link = Link(fromNode, toNode, 1)
        self.nodes[fromNodeKey].links.append(link)


    def print(self):
        for k, v in self.nodes.items():
            print(k, v.links)

if __name__ == '__main__':
    foo = Graph("tinyG.txt")
    foo.print()

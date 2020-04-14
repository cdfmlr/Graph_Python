import csv
import heapq
import numpy as np
from imageio import imwrite
from collections import deque


class Graph:
    def __init__(self):
        self.E = 0
        self.V = 0
        self.adj = {}

    def add_edge(self, v, u):
        if self.adj.get(v) is None:
            self.adj[v] = []
        self.adj[v].append(u)

    def initFromFile(self, fileName):
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

    def itervertices(self):
        return self.adj.keys()

    def neighbors(self, v):
        return  self.adj.get(v, [])
            
    def getAdjacencyMatrix(self):
        adjacencyMatrix = np.zeros((self.V, self.V))
        for k, v in self.adj.items():
            for i in v:
                adjacencyMatrix[k][i] = 1
        return adjacencyMatrix

    def print(self):
        adjacencyMatrix = self.getAdjacencyMatrix()
        print(adjacencyMatrix)

    def toImage(self, fileName):
        adjacencyMatrix = self.getAdjacencyMatrix()
        imwrite(fileName, adjacencyMatrix)

    def bfs(self, s):
        class BFSResult:
            def __init__(self):
                self.level = {}
                self.parent = {}

        r = BFSResult()
        r.parent = {s: None}
        r.level = {s: 0}

        queue = deque()
        queue.append(s)

        while queue:
            u = queue.popleft()
            for n in self.adj.get(u, []):
                if not r.level.get(n):
                    r.parent[n] = u
                    r.level[n] = r.level[u] + 1
                    queue.append(n)
        return r

    def dfs(self):
        class DFSResult:
            def __init__(self):
                self.parent = {}
                self.start_time = {}
                self.finish_time = {}
                self.edges = {}     # Edge classification for directed graph.
                self.order = []
                self.t = 0

        def dfs_visit(g, v, results, parent = None):
            results.parent[v] = parent
            results.t += 1
            results.start_time[v] = results.t
            if parent:
                results.edges[(parent, v)] = 'tree'

            for n in g.neighbors(v):
                if n not in results.parent:
                    dfs_visit(self, n, results, v)
                elif n not in results.finish_time:
                    results.edges[(v, n)] = 'back'
                elif results.start_time[v] < results.start_time[n]:
                    results.edges[(v, n)] = 'forward'
                else:
                    results.edges[(v, n)] = 'cross'

            results.t += 1
            results.finish_time[v] = results.t
            results.order.append(v)
    
        # DFS main
        results = DFSResult()
        for vertex in self.itervertices():
            if vertex not in results.parent:
                dfs_visit(self, vertex, results)
        return results
        
    def mstPrim(self, root):
        MAX = 9999999
        w = {}
        key = {}
        pi = {}
        Q = []
        for u in self.adj.keys():
            key[u] = MAX
            pi[u] = None
            heapq.heappush(Q, u)
        
        key[root] = 0
        
        while Q:
            u = heapq.heappop(Q)
            for v in self.adj[u]:
                w[(u, v)] = 1       # 权重
                if (v in Q) and (w[(u, v)] < key[v]):
                    pi[v] = u
                    key[v] = w[(u, v)]

        return pi


if __name__ == "__main__":
    foo = Graph()
    foo.initFromFile("tinyG.txt")

    # print(foo.V, foo.E)
    # foo.print()
    # foo.toImage("mediumG.png")

    # print(foo.bfs(0).level)
    
    # print(foo.dfs().order)
    print(foo.mstPrim(0))

class Digraph:
    def __init__(self , V):
        self.V = V
        self.E = 0
        self.adjList = {}
        for i in range(V):
            self.adjList[i] = []

    def addEdge(self , frm , to):
        self.adjList[frm].append(to)
        self.E += 1
    
    def numberOfVertices(self):
        return self.V
    
    def neighbours(self , v):
        return self.adjList[v]
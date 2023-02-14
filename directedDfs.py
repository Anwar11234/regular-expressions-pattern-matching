class DirectedDFS:
    def __init__(self , g):
        self.marked = [False] * g.numberOfVertices()

    def dfsSingleSource(self , g , src):
        self.dfs(g , src)

    def dfsMultipleSource(self, g , sources):
        for src in sources:
            if not self.marked[src]:
                self.dfs(g , src)
    
    def dfs(self ,g , start):
        self.marked[start] = True
        for v in g.neighbours(start):
            if not self.marked[v]:
                self.dfs(g , v)
    
    def reachable(self , vertex):
        return self.marked[vertex]
from directedDfs import DirectedDFS
from digraph import Digraph
class NFA:
    def __init__(self , regex):
        self.re = list(regex)
        self.numberOfStates = len(regex) + 1
        self.g =  self.buildEpsilonTransitionDigraph()

    def recognises(self,string):
        reachableStates = []
        dfs = DirectedDFS(self.g)
        dfs.dfsSingleSource(self.g , 0)

        for state in range(self.numberOfStates):
            if dfs.reachable(state):
                reachableStates.append(state)
        
        for i in range(len(string)):
            states = []
            for state in reachableStates:
                if state == len(self.re):
                    continue
                if self.re[state] == string[i] or self.re[state] == '.':
                    states.append(state + 1)
            
            dfs = DirectedDFS(self.g)
            dfs.dfsMultipleSource(self.g , states)
            reachableStates = []
            for state in range(self.numberOfStates):
                if dfs.reachable(state):
                    reachableStates.append(state)
        
        for state in reachableStates:
            if state == len(self.re):
                return True
        return False
    
    def buildEpsilonTransitionDigraph(self):
        g = Digraph(self.numberOfStates)
        ops = []
        for i in range(len(self.re)):
            leftParentethes = i
            if self.re[i] == '(' or self.re[i] == '|':
                ops.append(i)
            
            elif self.re[i] == ')':
                orIndex = ops.pop()
                if self.re[orIndex] == '|':
                    leftParentethes = ops.pop()
                    g.addEdge(leftParentethes , orIndex + 1)
                    g.addEdge(orIndex , i)
                else:
                    leftParentethes = orIndex
            
            if i < len(self.re) - 1 and self.re[i+1] == '*':
                g.addEdge(leftParentethes , i + 1)
                g.addEdge(i + 1, leftParentethes )
            
            if self.re[i] == '(' or self.re[i] == '*' or self.re[i] == ')':
                g.addEdge(i, i+1)
        
        return g

nfa = NFA("((A*B|AC)*D)")
print(nfa.recognises("AAABACACACACD"))
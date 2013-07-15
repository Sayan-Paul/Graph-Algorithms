#Graph Implementation
import collections

class Graph(object):
    "Graph container"
    def __init__(self):
        self.nodes=list()
        self.edge=dict()
        
        self.color=dict()
        self.par=dict()
        self.time=0
        self.d=dict()
        self.f=dict()

        self.dfsl=list()
        
    def insert(self,a,b):
        "Insert edges into graph"
        if not (a in self.nodes):
            self.nodes.append(a)
            self.edge[a]=list()
        if not (b in self.nodes):
            self.nodes.append(b)
            self.edge[b]=list()
        self.edge[a].append(b)
        self.edge[b].append(a)
        
    def succ(self,a):
        """Returns list of succesoors of cuurent node if present in graph
            else returns None"""
        try:
            return self.edge[a]
        except:
            return None

    def getnodes(self):
        "Returns list of nodes in graph"
        return self.nodes

    def dfs(self):
        "Depth first search algorithm"
        
        if not self.dfsl==[]:
            return
        
        for u in self.nodes:
            self.color[u]="white"
            self.par[u]=None
        self.time=0
        for u in self.nodes:
            if self.color[u]=="white":
                self.dfs_visit(u)
    def dfs_visit(self,u):
        self.time+=1
        self.dist=self.time
        self.color[u]="grey"
        for v in self.succ(u):
            if self.color[v]=="white":
                self.par[v]=u
                self.dfs_visit(v)
        self.color[u]="black"
        self.time+=1
        self.dfsl.append(u)
        self.f[u]=self.time

    def bfs(self):
        pass
        
        
    

## Driver code
if __name__=='__main__':
    graph=Graph()
    print "Enter edges of graph [Enter 0 0 to end]"
    while True:
        a,b=raw_input().split()
        if a=='0' or b =='0' :
            break
        graph.insert(a,b)
    print graph.getnodes()
    print [graph.succ(x) for x in graph.nodes]
    graph.dfs()
    print "Depth first search:",graph.dfsl

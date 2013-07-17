#Graph Implementation
#Author : Sayan Paul

import heapq,collections

class PriorityQueue:
    """
      Implements a priority queue data structure.
    """
    def  __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def search(self,element):
        for priority,count,item in self.heap:
            if item == element:
                return True
        return False

    def update(self,element,priorityNew):
        l=[]
        for priority,count,item in self.heap:
            if item == element:
                l.append(tuple([priorityNew,count,item]))
            else : l.append(tuple([priority,count,item]))
        self.heap=l
        heapq.heapify(self.heap)

class Graph(object):
    "Undirected Unweighted Graph container"
    def __init__(self):
        self.nodes=list()
        self.edge=dict()
        
        self.color=dict()
        self.par=dict()
        self.time=0
        self.d=dict()
        self.f=dict()

        self.dfsl=list()
        self.bfsl=list()
        
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
        """Returns list of successors of cuurent node if present in graph
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
        
        self.dfsl.append(u)## node Discovered
        
        self.dist=self.time
        self.color[u]="grey"
        for v in self.succ(u):
            if self.color[v]=="white":
                self.par[v]=u
                self.dfs_visit(v)
        self.color[u]="black"
        self.time+=1
        self.f[u]=self.time

    def bfs(self,s):
        q=list()
        for u in self.nodes:
            self.color[u]="white"
            self.par[u]=None
        self.color[s]="grey"
        self.d[s]=0
        q.append(s)
        while q!=[]:
            u=q.pop(0)
            for v in self.succ(u):
                if self.color[v]=="white":
                    self.color[v]="grey"
                    self.d[v]=self.d[u]+1
                    self.par[v]=u
                    q.append(v)
            self.color[u]="black"
            self.bfsl.append(u)
        
class UWGraph(Graph):
    "Undirected Weighted Graph container"

    def __init__(self):
        self.nodes=list()
        self.edge=dict()
        
        self.color=dict()
        self.par=dict()
        self.time=0
        self.d=dict()
        self.f=dict()

        self.dfsl=list()
        self.bfsl=list()
        self.rank=dict()
        self.edges_w=list()
        self.key=dict()
    
    def succ(self,a):
        """Returns list of successors of cuurent node if present in graph
            else returns None"""
        try:
            return self.edge[a].keys()
        except:
            return None


    def succ_w(self,a):
        """Returns list of successors of cuurent node with weight if present in graph
            else returns None"""
        try:
            return self.edge[a]
        except:
            return None

    def insert(self,a,b,w):
        "Insert edges into graph"
        if not (a in self.nodes):
            self.nodes.append(a)
            self.edge[a]=dict()
        if not (b in self.nodes):
            self.nodes.append(b)
            self.edge[b]=dict()
        self.edge[a][b]=w
        self.edge[b][a]=w
        self.edges_w.append(tuple([a,b,w]))

    def find(self,v):
        "Returns root of tree to which v belongs"
        if self.par[v]!=v:
            self.par[v]=self.find(self.par[v])
        return self.par[v]

    def union(self,v1,v2):
        "Joins the trees to which v1 and v2 belong"
        r1=self.find(v1)
        r2=self.find(v2)
        if r1!=r2:
            if self.rank[r1]>self.rank[r2]:
                self.par[r2]=r1
            else:
                self.par[r1]=r2
                if self.rank[r1]==self.rank[r2]:
                    self.rank[r2]+=1

    def kruskal(self):
        "Kruskal's Algorithm"
        rank=dict()
        for v in self.nodes:
            self.par[v]=v
            self.rank[v]=0

        mst=set()
        self.edges_w.sort(key=lambda x : x[2])
        for edge in self.edges_w:
            v1,v2,w=edge
            if self.find(v1)!=self.find(v2):
                self.union(v1,v2)
                mst.add(edge)
        return mst

    def prim(self,r):
        "Prim's Algorithm"
        q=PriorityQueue()
        for v in self.nodes:
            self.key[v]=10**6               #this chosen as the upper limit of weights [Can be changed as required]
            self.par[v]=None
            if v!=r:
                q.push(v,self.key[v])
        self.key[r]=0
        q.push(r,self.key[r])
        while not q.isEmpty():
            u=q.pop()
            adj=self.succ_w(u)
            for v in adj:
                if q.search(v) and adj[v]<self.key[v]:
                    self.par[v]=u
                    self.key[v]=adj[v]
                    q.update(v,self.key[v])
        print str(self.par)

    def Floyd_Warshall(self):
        dis=dict()
        for u in self.nodes:
            t=dict()
            adj=self.succ_w(u)
            for v in self.nodes:
                if v==u:
                    t[v]=0
                else:
                    t[v]=adj[v]
            dis[u]=dict(t)
        for k in self.nodes:
            for i in self.nodes:
                for j in self.nodes:
                    if dis[i][k] + dis[k][j] < dis[i][j]:
                        dis[i][j] = dis[i][k] + dis[k][j]
        print "Distance Matrix :"
        for u in self.nodes:
            print u ,str(dis[u])
        

class DUGraph(Graph):
    "Directed Unweighted Graph Container"

    def insert(self,a,b):
        "Insert edges into graph"
        if not (a in self.nodes):
            self.nodes.append(a)
            self.edge[a]=list()
        if not (b in self.nodes):
            self.nodes.append(b)
            self.edge[b]=list()
        self.edge[a].append(b)

class DWGraph(UWGraph):
    "Directed Weighted Graph Container"

    def insert(self,a,b,w):
        "Insert edges into graph"
        if not (a in self.nodes):
            self.nodes.append(a)
            self.edge[a]=dict()
        if not (b in self.nodes):
            self.nodes.append(b)
            self.edge[b]=dict()
        self.edge[a][b]=w
        self.edges_w.append(tuple([a,b,w]))

    def Bellman_Ford(self,s):
        """This implementation takes in a graph, represented as lists of vertices and edges,
    and fills two arrays (distance and predecessor) with shortest-path information"""
        for v in self.nodes:
            if v==s:
                self.d[v]=0
            else:
                self.d[v]=10**7
            self.par[v]=None  
        for i in range(1,len(self.nodes)):
            for u,v,w in self.edges_w:
                if self.d[v]>self.d[u]+w:
                    self.d[v]=self.d[u]+w
                    self.par[v]=u
        for u,v,w in self.edges_w:
                if self.d[v]>self.d[u]+w:
                    print "[ERROR] Graph contains a negative-weight cycle"
                    return
        print "Parent list:",str(self.par)
        print "Distance from source:",str(self.d)
        
    def Dijkstra(self,r):
        "Dijksta's Algorithm for single source shortest path"
        q=PriorityQueue()
        for v in self.nodes:
            self.d[v]=10**6               #this chosen as the upper limit of weights [Can be changed as required]
            self.par[v]=None
            if v!=r:
                q.push(v,self.d[v])
        self.d[r]=0
        q.push(r,self.d[r])
        while not q.isEmpty():
            u=q.pop()
            if self.d[u]==10**6:
                break
            adj=self.succ_w(u)
            for v in adj:
                if self.d[v]>self.d[u]+adj[v]:
                    self.d[v]=self.d[u]+adj[v]
                    self.par[v]=u
                    q.update(v,self.d[v])
        print "Parent list:",str(self.par)
        print "Distance from source:",str(self.d)
            


## Driver code
if __name__=='__main__':
    n=input("""Enter Choice:\n1. Undirected Unweighted Graph\n2. Undirected Weighted Graph
3. Directed Unweighted Graph\n4. Directed Weighted Graph\n\n$Graph\_ """)


    
    if n==1:
        graph=Graph()
        print "Enter edges of graph [Enter 0 0 to end]"
        while True:
            a,b=raw_input().split()
            if a=='0' or b =='0' :
                break
            graph.insert(a,b)
    ##    print graph.getnodes()
    ##    print [graph.succ(x) for x in graph.nodes]
        m=input("Enter Choice:\n1. Depth First Search\n2. Breadth First Search\n\n$Graph\_ ")

        if m==1:
            graph.dfs()
            print "Depth First Search:",graph.dfsl
        elif m==2:
            graph.bfs(graph.nodes[0])
            print "Breadth First Search:",graph.bfsl


            
    elif n==2:
        graph=UWGraph()
        print "Enter edges of graph [Enter 0 0 0 to end]"
        while True:
            a,b,w=raw_input().split()
            if a=='0' or b =='0' or w=='0':
                break
            graph.insert(a,b,int(w))
        #print [graph.succ_w(x) for x in graph.nodes]
        
        m=input("""Enter Choice:\n1. Depth First Search
2. Breadth First Search\n3. Kruskal Minimum Spanning Tree\n4. Prim's Minimum Spanning Tree\n\n$Graph\_ """)
        if m==1:
            graph.dfs()
            print "Depth First Search:",graph.dfsl
        elif m==2:
            graph.bfs(graph.nodes[0])
            print "Breadth First Search:",graph.bfsl
        elif m==3:
            print "Minimum Spanning Tree [Edge list]:\n",graph.kruskal()
        elif m==4:
            print "Minimum Spanning Tree [Parent list]:\n"
            graph.prim(graph.nodes[0])

    elif n==3:
        graph=DUGraph()
        print "Enter edges of graph [Enter 0 0 to end]"
        while True:
            a,b=raw_input().split()
            if a=='0' or b =='0' :
                break
            graph.insert(a,b)
    ##    print graph.getnodes()
    ##    print [graph.succ(x) for x in graph.nodes]
        m=input("Enter Choice:\n1. Depth First Search\n2. Breadth First Search\n\n$Graph\_ ")

        if m==1:
            graph.dfs()
            print "Depth First Search:",graph.dfsl
        elif m==2:
            graph.bfs(graph.nodes[0])
            print "Breadth First Search:",graph.bfsl

    elif n==4:
        graph=DWGraph()
        print "Enter edges of graph [Enter 0 0 0 to end]"
        while True:
            a,b,w=raw_input().split()
            if a=='0' or b =='0' or w=='0':
                break
            graph.insert(a,b,int(w))
        #print [graph.succ_w(x) for x in graph.nodes]
        
        m=input("""Enter Choice:\n1. Depth First Search
2. Breadth First Search\n3. Bellman Ford Single Source Shortest Path\n3. Dijkstra Single Source Shortest Path\n\n$Graph\_ """)
        if m==1:
            graph.dfs()
            print "Depth First Search:",graph.dfsl
        elif m==2:
            graph.bfs(graph.nodes[0])
            print "Breadth First Search:",graph.bfsl
        elif m==3:
            c=raw_input("Enter source: ")
            graph.Bellman_Ford(c)
        elif m==4:
            c=raw_input("Enter source: ")
            graph.Dijkstra(c)

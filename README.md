Graph-Algorithms
================

Python implementation of graph structure and some common algorithms

A graph is a representation of a set of objects where some pairs of objects are connected by links. The interconnected objects are represented by mathematical abstractions called vertices, and the links that connect some pairs of vertices are called edges. Typically, a graph is depicted in diagrammatic form as a set of dots for the vertices, joined by lines or curves for the edges. 
The edges may be directed or undirected.

Breadth First Search:
-----------------------

In graph theory, breadth-first search (BFS) is a strategy for searching in a graph when search is limited to essentially two operations: (a) visit and inspect a node of a graph; (b) gain access to visit the nodes that neighbor the currently visited node. The BFS begins at a root node and inspects all the neighboring nodes. Then for each of those neighbor nodes in turn, it inspects their neighbor nodes which were unvisited, and so on. Compare BFS with the equivalent, but more memory-efficient Iterative deepening depth-first search and contrast with depth-first search.

Psuedocode:

		1  procedure BFS(G,v):
		2      create a queue Q
		3      enqueue v onto Q
		4      mark v
		5      while Q is not empty:
		6          t ? Q.dequeue()
		7          if t is what we are looking for:
		8              return t
		9          for all edges e in G.adjacentEdges(t) do
		10             u ? G.adjacentVertex(t,e)
		11             if u is not marked:
		12                  mark u
		13                  enqueue u onto Q
		14     return none

Depth First Search:
----------------------

Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. One starts at the root (selecting some node as the root in the graph case) and explores as far as possible along each branch before backtracking.

Psuedocode:

		1  procedure DFS(G,v):
		2      label v as explored
		3      for all edges e in G.adjacentEdges(v) do
		4          if edge e is unexplored then
		5              w ? G.adjacentVertex(v,e)
		6              if vertex w is unexplored then
		7                  label e as a discovery edge
		8                  recursively call DFS(G,w)
		9              else
		10                 label e as a back edge

Kruskal's algorithm:
----------------------

Kruskal's algorithm is a greedy algorithm in graph theory that finds a minimum spanning tree for a connected weighted graph. This means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized. If the graph is not connected, then it finds a minimum spanning forest (a minimum spanning tree for each connected component).

Psuedocode:

		KRUSKAL(G):
		1 A = �
		2 foreach v ? G.V:
		3   MAKE-SET(v)
		4 foreach (u, v) ordered by weight(u, v), increasing:
		5    if FIND-SET(u) ? FIND-SET(v):
		6       A = A ? {(u, v)}
		7       UNION(u, v)
		8 return A

Prim's algorithm:
----------------------

In computer science, Prim's algorithm is a greedy algorithm that finds a minimum spanning tree for a connected weighted undirected graph. This means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized. 

Psuedocode:


    :(initializations).
    O={1} (V(1) root of the T tree).
    P={2,...,n}
    For every j belonging to P :e(j):=c[e(j1)] , p(j)=1
    ( all peaks connected to the root.By definition of the cost function:e(j)=infinite when V(j) does not connect to V(1).).
    Choose a k for which e(k)<=e(j) for every j belonging to P.In case of tight choose the smaller one.
    Exchange the O set with the set produced by the union of the O set and {k} . Exchange the P set with the set produced by the difference of the P set and {k} .(P<-P-{k}) If P=0 then stop.
    For every j belonging to P compare e(j) with c[e(kj)].
    If e(j) >c[e(kj)] exchange e(j) <-c(e(kj)).Go back to Step 1.

Dijkstra's algorithm:
----------------------

For a given source vertex (node) in the graph, the algorithm finds the path with lowest cost (i.e. the shortest path) between that vertex and every other vertex. It can also be used for finding costs of shortest paths from a single vertex to a single destination vertex by stopping the algorithm once the shortest path to the destination vertex has been determined. For example, if the vertices of the graph represent cities and edge path costs represent driving distances between pairs of cities connected by a direct road, Dijkstra's algorithm can be used to find the shortest route between one city and all other cities.

Psuedocode:

		 1  function Dijkstra(Graph, source):
		 2      for each vertex v in Graph:                                // Initializations
		 3          dist[v] := infinity ;                                  // Unknown distance function from 
		 4                                                                 // source to v
		 5          previous[v] := undefined ;                             // Previous node in optimal path
		 6      end for                                                    // from source
		 7      
		 8      dist[source] := 0 ;                                        // Distance from source to source
		 9      Q := the set of all nodes in Graph ;                       // All nodes in the graph are
		10                                                                 // unoptimized - thus are in Q
		11      while Q is not empty:                                      // The main loop
		12          u := vertex in Q with smallest distance in dist[] ;    // Source node in first case
		13          remove u from Q ;
		14          if dist[u] = infinity:
		15              break ;                                            // all remaining vertices are
		16          end if                                                 // inaccessible from source
		17          
		18          for each neighbor v of u:                              // where v has not yet been 
		19                                                                 // removed from Q.
		20              alt := dist[u] + dist_between(u, v) ;
		21              if alt < dist[v]:                                  // Relax (u,v,a)
		22                  dist[v] := alt ;
		23                  previous[v] := u ;
		24                  decrease-key v in Q;                           // Reorder v in the Queue
		25              end if
		26          end for
		27      end while
		28      return dist;
		29  endfunction

Floyd Warshall algorithm:
--------------------------

In computer science, the Floyd�Warshall algorithm (also known as Floyd's algorithm, Roy�Warshall algorithm, Roy�Floyd algorithm, or the WFI algorithm) is a graph analysis algorithm for finding shortest paths in a weighted graph with positive or negative edge weights (but with no negative cycles, see below) and also for finding transitive closure of a relation R. A single execution of the algorithm will find the lengths (summed weights) of the shortest paths between all pairs of vertices, though it does not return details of the paths themselves.

Psuedocode:

		let dist be a |V| � |V| array of minimum distances initialized to 8 (infinity)
		for each vertex v
		   dist[v][v] ? 0
		for each edge (u,v)
		   dist[u][v] ? w(u,v)  // the weight of the edge (u,v)
		for k from 1 to |V|
		   for i from 1 to |V|
			  for j from 1 to |V|
				 if dist[i][k] + dist[k][j] < dist[i][j] then
					dist[i][j] ? dist[i][k] + dist[k][j]

This file can be used in any program like a python module using import
------------------------------------------------------------------------

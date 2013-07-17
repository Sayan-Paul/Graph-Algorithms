Graph-Algorithms
================

Python implementation of graph structure and some common algorithms

A graph is a representation of a set of objects where some pairs of objects are connected by links. The interconnected objects are represented by mathematical abstractions called vertices, and the links that connect some pairs of vertices are called edges.[1] Typically, a graph is depicted in diagrammatic form as a set of dots for the vertices, joined by lines or curves for the edges. 
The edges may be directed or undirected.

Breadth First Search:
======================

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

Breadth First Search:
======================

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


"""
  Iterative Depth-First Search
  Stack - LIFO - pop()
"""
# * For all type of graphs
from operator import ne


def dfsGraphsTraversal(graph, start):
  stack, path = [start], []

  while stack:
    vertex = stack.pop()
    if vertex in path:
      continue
    path.append(vertex)

    for neighbor in graph[vertex]:
      stack.append(neighbor)
  return path

adjacency_matrix = {
  1: [2, 3], 
  2: [4, 5],
  3: [5], 
  4: [6], 
  5: [6],
  6: [7], 
  7: []
}
print("Path: ", dfsGraphsTraversal(adjacency_matrix, 1))
# [1, 3, 5, 6, 7, 2, 4]
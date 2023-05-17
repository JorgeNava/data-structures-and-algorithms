"""
  Breadth-Frist Search iterative
  Queue - FIFO - pop(0)
"""
def bfsGraphsTraversal(tree, vertex):
  queue, path = [vertex], [vertex]
  
  while queue:
    actNode = queue.pop(0)
    for neighbor in tree[actNode]:
      if neighbor not in path:
        path.append(neighbor)
        queue.append(neighbor)
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

print("Path: ", bfsGraphsTraversal(adjacency_matrix, 1))
# [1, 2, 3, 4, 5, 6, 7]
"""
  Breadth-Frist Search recursive
  Queue - FIFO - pop(0)
"""
def bfsGraphsTraversal(tree, queue, path):
  if queue:
    actNode = queue.pop(0)
    for neighbor in tree[actNode]:
      if neighbor not in path:
        path.append(neighbor)
        queue.append(neighbor)
    bfsGraphsTraversal(tree, queue, path)
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

startNode = 1
queue, path = [startNode], [startNode]
print("Path: ", bfsGraphsTraversal(adjacency_matrix, queue, path))
# [1, 2, 3, 4, 5, 6, 7]
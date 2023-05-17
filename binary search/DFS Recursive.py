"""
  Recursive Depth-First Search
"""
class BinaryTreeNode():
  def __init__(self, value, left = None, right = None):
    self.value = value
    self.left = left
    self.right = right

  def __str__(self):
    return "BinaryTreeNode("+ str(self.value) +")"

# * Only for binary trees
def dfsBinaryTraversal(actNode, path = []):
  if actNode is not None:
    if actNode not in path:
      path.append(actNode.value)
      dfsBinaryTraversal(actNode.left, path)
      dfsBinaryTraversal(actNode.right, path)
      return path

# * For all type of graphs
def dfsGraphsTraversal(graph, vertex, path=[]):
  path.append(vertex)
  for neighbor in graph[vertex]:
    if neighbor not in path:
      path = dfsGraphsTraversal(graph, neighbor, path)
  return path

tree = BinaryTreeNode('A', BinaryTreeNode('B', BinaryTreeNode('D'), BinaryTreeNode('E')), BinaryTreeNode('C', BinaryTreeNode('F'), BinaryTreeNode('G')))
adjacency_matrix = {
  1: [2, 3], 
  2: [4, 5],
  3: [5], 
  4: [6], 
  5: [6],
  6: [7], 
  7: []
}
print(dfsBinaryTraversal(tree))
print("Path: ", dfsGraphsTraversal(adjacency_matrix, 1))
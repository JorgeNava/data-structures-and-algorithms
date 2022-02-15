#Write a function that, given a binary tree of integers, returns the sums of all the root-to-leaf paths.

#Input:
#         2
#       /  \
#     3     5
#    / \
#   1   5
#
# Output: 
# [6, 10, 7]

class Node():
  def __init__(self, val=None, leftChild=None, rightChild=None):
    self.leftChild = leftChild
    self.rightChild = rightChild
    self.val = val
  
  def __str__(self):
    return "Node " + self.val

  # Aux functions
  def hasLeftChild(self):
    return self.leftChild is not None
  def hasRightChild(self):
    return self.rightChild is not None

def myAlgo(node, sumOfPath = 0, sumOfLeafs = []):
  sumOfPath += node.val 
  if node.hasLeftChild():
    myAlgo(node.leftChild, sumOfPath, sumOfLeafs)
  if node.hasRightChild():
    myAlgo(node.rightChild, sumOfPath, sumOfLeafs)
  if not node.hasLeftChild() and not node.hasRightChild():
    sumOfLeafs.append(sumOfPath)
    sumOfPath = 0
  return sumOfLeafs

tree = Node(2, Node(3, Node(1), Node(5)), Node(5))
print(myAlgo(tree))
"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""

class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None
  
  def add(self, data):
    newNode = ListNode(data)
    if not self.head:
      self.head = newNode
      return
    currentNode = self.head
    while currentNode.next:
      currentNode = currentNode.next
    currentNode.next = newNode
  
  def printList(self):
    currentNode = self.head
    while currentNode:
      print(currentNode.val)
      currentNode = currentNode.next

  def nums(self):
    nums = []
    currentNode = self.head
    while currentNode:
      nums.append(currentNode.val)
      currentNode = currentNode.next
    return nums
    
"""
  Convert linked lists into arrays
  Order concatanated arrays
  Convert array into linked list
"""

def getList(list1, list2):
  l1 = LinkedList()
  l2 = LinkedList()
  
  for number in list1:
    l1.add(number)
  for number in list2:
    l2.add(number)

  arr1 = []
  arr2 = []
  current = l1.head
  while current:
    arr1.append(current.val)
    current = current.next
  current = l2.head
  while current:
    arr2.append(current.val)
    current = current.next

  arr = arr1 + arr2
  arr.sort()

  output = LinkedList()
  for num in arr:
    output.add(num)
  return output

tests = [
  {
    "list1": [1,2,4],
    "list2": [1,3,4],
    "output": [1,1,2,3,4,4]
  },
  {
    "list1": [],
    "list2": [],
    "output": []
  },
  {
    "list1": [],
    "list2": [0],
    "output": [0]
  },
]
for test in tests:
  output = getList(test["list1"], test["list2"])
  print(output.nums())
  print('>',output.nums() == test["output"])
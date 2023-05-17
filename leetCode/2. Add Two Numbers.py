"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [0], l2 = [0]
Output: [0]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

numnum1String = [9, 9, 9, 9, 9, 9, 9]
numnum2String = [9, 9, 9, 9]
expectedOutput = [8, 9, 9, 9, 0, 0, 0, 1]


class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def printList(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


""" Notes:
	> We could try to concatenate as a string all values in the linked list
	> we would get the two final numbers and we could cast them into ints
	> and then add them.
	> Once we have the sum, we convert extract each of its digits and store
	> them in a new linked list.

	> We need to itereate through the list in an inverse oreder or try to
	> iterate through it but re-order the numbers.

	> Time complexity of O(n) since we only iterate through the linked list constant times (3)
	> Space complexity of O(n) since we created 3 arrays that will have the same lenght as the inputed lists
"""

l1 = LinkedList()
l2 = LinkedList()
num1 = []
num2 = []
num1String = ''
num2String = ''
output = []
linkedListOutput = LinkedList()


for n in numnum1String:
    l1.add(n)
for n in numnum2String:
    l2.add(n)

current = l1.head
while current:
    num1.insert(0, current.data)
    current = current.next
    num1String = str(num1[0]) + num1String
current = l2.head
while current:
    num2.insert(0, current.data)
    current = current.next
    num2String = str(num2[0]) + num2String
rslt = str(int(num1String) + int(num2String))

# print(num1String)
# print(num2String)
# print(rslt)

rslt = list(rslt)
for i in range(len(rslt)):
    output.append(int(rslt[len(rslt) - i - 1]))
    linkedListOutput.add(int(rslt[len(rslt) - i - 1]))


print('Expected Output:', expectedOutput)
print('Output:', output)
print('Worked:', expectedOutput == output)

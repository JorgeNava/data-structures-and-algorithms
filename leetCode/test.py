"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""
def getIndexes(nums, target):
    """
      {
        7: 0
      } - [0,1]
      {
        3: 0,
        4: 1,
      } - [1,2]
      {
        3: 0
      } - [0,1]
      Iterate through the array
      For each one:
        Get the diff between target and actNum
        If actNum in aux:
          return diff index and actNum index
        else:
          set diff as key and actNum index in aux
    """
    output = []
    aux = {}
    for i in range(len(nums)):
      actNum = nums[i]
      diff = target - actNum
      if actNum in aux:
        output = [aux[actNum], i]
        break
      else:
        aux[diff] = i
    return output

tests = [
  {
    "nums": [2,7,11,15],
    "target": 9,
    "correctOutput": [0,1]
  },
  {
    "nums": [3,2,4],
    "target": 6,
    "correctOutput": [1,2]
  },
  {
    "nums": [3,3],
    "target": 6,
    "correctOutput": [0,1]
  },
  {
    "nums": [3,3,7,1,10,23,7,9,6,0,-1,6],
    "target": 13,
    "correctOutput": [1,4]
  }
]
for test in tests:
  output = getIndexes(test["nums"], test["target"])
  print(output)
  print('>',output == test["correctOutput"])
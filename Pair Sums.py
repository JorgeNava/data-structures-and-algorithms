"""
Given a list of n integers arr[0..(n-1)], determine the number of different pairs of elements within it which sum to k.
If an integer appears in the list multiple times, each copy is considered to be different; that is, two pairs are considered different if one pair includes at least one array index which the other doesn't, even if they include the same values.
Signature
int numberOfWays(int[] arr, int k)
Input
n is in the range [1, 100,000].
Each value arr[i] is in the range [1, 1,000,000,000].
k is in the range [1, 1,000,000,000].
Output
Return the number of different pairs of elements which sum to k.
Example 1
n = 5
k = 6
arr = [1, 2, 3, 4, 3]
output = 2
The valid pairs are 2+4 and 3+3.
Example 2
n = 5
k = 6
arr = [1, 5, 3, 3, 3]
output = 4
There's one valid pair 1+5, and three different valid pairs 3+3 (the 3rd and 4th elements, 3rd and 5th elements, and 4th and 5th elements).
"""

def numberOfWays(arr, k):
  auxDict = {}
  for num in arr:
    if num in auxDict:
      auxDict[num] += 1
    else:
      auxDict[num] = 1
  
  count = 0
  for key in auxDict:
    diff =  k - key
    valueCount = auxDict[key]
    if diff in auxDict:
      if key == k / 2:
        count += valueCount * (valueCount - 1) / 2 
      else:
        count += valueCount / 2
  return count

tests = [
  {
    "arr": [1, 2, 3, 4, 3],
    "k": 6,
    "rslt": 2
  },
  {
    "arr": [1, 5, 3, 3, 3],
    "k": 6,
    "rslt": 4
  }
  
] 
for test in tests:
  print("Test list: ", test["arr"])
  print("Obtained result: ", numberOfWays(test["arr"], test["k"]))
  print("Real result: ", test["rslt"])
  print("TEST RESULT: ", numberOfWays(test["arr"], test["k"]) == test["rslt"])

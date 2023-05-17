"""
  Algoritm must make it in O(1)
  Cyclic-dependencies should be the best line of thought to
  solution this problem.
  Whats a cyclic-dependency?
    Cyclic dependencies occur when multiple modules or components in a software system depend on each other in a circular manner. 
"""

nums = [1, 2, 3, 4, 5, 6, 7]
expectedResult = [5, 6, 7, 1, 2, 3, 4]
k = 3


""" 
FIRST APPROACH - FAILED BECAUSE O(N)
numsLength = len(nums)
for i in range(k):
    temp = nums[-1]
    for numIndex in reversed(range(numsLength)):
        print('first', nums[numIndex])
        nums[numIndex] = nums[numIndex - 1]
        print('second', nums[numIndex])
    nums[0] = temp
"""

""" 
# GPT APPROACH - SUCCESS
# For example, let's consider the array [1, 2, 3, 4, 5, 6, 7] and k = 3. If we slice the array using k, we get [5, 6, 7] as the first part and [1, 2, 3, 4] as the second part. By concatenating these two parts, we get the rotated array [5, 6, 7, 1, 2, 3, 4].
# The modulo operation is used in this solution to handle the case where k is greater than the length of the array. If k is greater than the length of the array, it means that rotating the array by k steps is equivalent to rotating it by k % n steps.
n = len(nums)
k = k % n
print(k)
print(nums[n-k:])
print(nums[:n-k])
nums[:] = nums[n-k:] + nums[:n-k] 
"""

# ADAPTED VERSION
# Get the length of the array
numsLength = len(nums)
# Get the number numbers we should move to the right
# If its bigger than the length of the array then we get its modulo to determine how many
# numbers to move since we had to rotate completly the array (n = 8, k = 15, necesaryMoves = 7)
arrayDivider = k % numsLength
# Create slice of array that will be placed at the begining of the array (sliding them to the right)
firstSlice = nums[numsLength-arrayDivider:]
# Create slice of array that will be placed after the first array (moving them to the right)
lastSlice = nums[:numsLength-arrayDivider]
# Combine both slices of array to create the slided array to the right
# [:] is used to replace old list with the new one if it was sliced, without it it would create a reference
# to a new list with the concatation of the slices (won't be the same array)
nums[:] = firstSlice + lastSlice


print('\n============================================')
print('Final array: ', nums)
print('Test passed: ', nums == expectedResult)

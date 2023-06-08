"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]

Input: nums = [3,3,7,1,10,23,7,9,6,0,-1,6], target = 13
Output: [1,4]

Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?
"""
nums = [3,3,7,1,10,23,7,9,6,0,-1,6]
target = 13
expectedOutput = [1, 4]
output = []


""" NOTES:
  > register the difference between the i element and the target
  > move to the next element and get the difference
  > check if the actual element added with one of the previously registered values is equal the target
  > if its equal ding dong, if not repeat process

  ¿ how to register values, since we want to check all of the registered values per element in array
  ¿ if we want we itereate through every element with every elemnt of the array but that would give us a 0(n^2)
  ¿ we could try to store only the diff value thats shortest? No
  ¿ store in structure diff with its index?
  ¿ check if i is bigger than target, if its ignore it? No becuase negative values are acepted in array
  
  > store values in hashmap as keys and their indexes as values
  > get the complement of the actual element and search for it in the hashmap
  > since there cannot exist two exact same keys in a hashmap then if it already exists
  > we do not add it to the hashmap since it would replace the previous value
  > if it doesn't exist then we make sure its value (really the index) is not the same
  > as the one of the actual element.
  > If the complement exists in the hashmap and the index of it its not the actual element index
  > then we append the index of the complement and the actual element on the output array
  > This would gave an algorithm of O(n) on time complexity since we only iterate through the array once
  > and a O(n) on space complexity since we could need a hashmap as big as the nums array in the worst case
"""

hashMap = {}
for i in range(len(nums)):
    actualNum = nums[i]
    complement = target - actualNum
    if complement not in hashMap:
        hashMap[actualNum] = i
    # print('nums[i]', actualNum)
    # print('complement', complement)
    # print('hashMap', hashMap)
    if complement in hashMap and hashMap[complement] != i:
        # print('appending')
        output.append(hashMap[complement])
        output.append(i)
        break


print('Nums:', nums)
print('Target:', target)
print('Expected Output:', expectedOutput)
print('Output:', output)
print('Worked:', expectedOutput == output)

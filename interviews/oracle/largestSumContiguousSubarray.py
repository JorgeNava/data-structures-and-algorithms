""" 
Given an array arr[] of size N. The task is to find the sum of the contiguous subarray within a arr[] with the largest sum. 
(Kadane’s Algorithm)
Max sub-array is the act element alone or in sum with the prev max sub-array

Look at eah index and find the max sub-array ending at each index. O(n^2)

With Kadane:
Look at eah index and find the max sub-array ending at each index.
The local max sub-array is either the current element or the current element combined with the previous max sub-array
Except for the 1st element.
"""

def kadane(list):
  max_subarray = []
  max_current = max_global = list[0]
  for i in range(len(list)):
    max_current = max(list[i], max_current + list[i])
    if max_current > max_global:
      max_global = max_current
  return 

numbers = [-2,3,2,-1]
print(kadane(numbers))
""""
You are given an array A containing N integers. Your task is to find all subarrays whose average sum is greater than the average sum of the remaining array elements. You must return the start and end index of each subarray in sorted order.
A subarray that starts at position L1 and ends at position R1 comes before a subarray that starts at L2 and ends at R2 if L1 < L2, or if L1 = L2 and R1 ≤ R2.
Note that we'll define the average sum of an empty array to be 0, and we'll define the indicies of the array (for the purpose of output) to be 1 through N. A subarray that contains a single element will have L1 = R1.
Signature
Subarray[] aboveAverageSubarrays(int[] A)
Input
1 ≤ N ≤ 2,000
1 ≤ A[i] ≤ 1,000,000
Output
A Subarray is an object with two integer fields, left and right, defining the range that a given subarray covers. Return a list of all above-average subarrays sorted as explained above.
Example 1
A = [3, 4, 2]
output = [[1, 2], [1, 3], [2, 2]]
The above-average subarrays are [3, 4], [3, 4, 2], and [4].
"""
def myAlgo(A):
  #Get the totalSum of the array and then use the double cicle to iterate through every array
  #We are goint to get the sum of every sub array and compare it to the avg of the totalSum with the missing number of values to check
  #To get the number of missing value to check will git it from the diference between the ones we'be iterate through and the total elements of the array
  totalSum = sum(A)
  rslt = [] 
  for i in range(len(A)):
    for j in range(i, len(A)):
      subTotal = sum(A[i:j+1])
      n = j + 1 - i
      if ((totalSum - subTotal) / (len(A) - n if n != len(A) else -1)) < subTotal / n:
        rslt.append([i+1,j+1])
  return rslt
A = [3, 4, 2]
print(myAlgo(A))
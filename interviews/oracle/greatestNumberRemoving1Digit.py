""" 
Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.
Example
    For n = 152, the output should be
    solution(n) = 52;
    For n = 1001, the output should be
    solution(n) = 101.

Input/Output
    [execution time limit] 3 seconds (java)

    [input] integer n

    Guaranteed constraints:
    10 ≤ n ≤ 10^6.

    [output] integer 
"""

def getHighestNumber(n):
  number = str(n)
  max = 10
  
  if len(number) <= 2:
    if int(number[0]) > int(number[1]):
      return number[0]
    if int(number[1]) > int(number[0]):
      return number[1]
  
  for i in range(len(number)):
    if i - 1 <= 0:
      leftSNumber = ''
    else:
      leftSNumber = number[:i]
      
    if i + 1 >= len(number):
      rightSNumber = ''
    else: 
      rightSNumber = number[i+1:]

    completeNumber = int(leftSNumber + rightSNumber)

    if completeNumber > max:
      max = completeNumber
  return max

print(getHighestNumber(152))
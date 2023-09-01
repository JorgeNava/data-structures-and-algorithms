""" 
Given a number x, determine whether the given number is Armstrong’s number or not.

A positive integer of n digits is called an Armstrong number of order n (order is the number of digits) if

abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + .... 

Example: 
Input:153
Output: Yes
153 is an Armstrong number.
1*1*1 + 5*5*5 + 3*3*3 = 153
"""

x = 153
s = str(x)
count = 0

n = len(s)
for digit in s:
  count += int(digit) ** n
print(count == x)
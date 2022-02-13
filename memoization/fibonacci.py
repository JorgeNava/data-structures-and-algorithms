"""
  Next step in optimization will be to
  avoid calling recursive functions as
  in linte 13.
  ACTUAL COMPLEXITY: LINEAR
  But stack memory limit can be reached easily
"""
def momoizedFibonacci(n, memo):
  if n in memo: # Check if value was already calculated
    return memo[n]
  if n <= 1:
    memo[n] = n # Store calculated value
    return n
  else:
    memo[n] = momoizedFibonacci(n-1, memo) + momoizedFibonacci(n-2, memo)
    return memo[n]

# Compared to recursive method is way faster
memo = {}
print("momoizedFibonacci: ", momoizedFibonacci(10, memo))

"""
  Here the cost is LINEAR because we removed the recusivity
  and now without the risk of getting to the limit of the stack memory
"""
def linearFibonacci(n):
  memo = {0: 1, 1: 1}
  for i in range(2,n):
    memo[i] = memo[i - 1] + memo[i - 2]
  return memo[n-1]

# Compared to recursive method is way faster
print("linearFibonacci: ", linearFibonacci(10))
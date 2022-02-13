"""
  Better that recursive fibonacci it doesn't needs to call 
  the same function again. We avoid repeating calculations.
"""

def fibonacci(n):
  a, b = 0, 1
  for i in range(n):
    a, b = b, a + b
  return a,b

print(fibonacci(7))
data = [1,2,4,23,76,452] # In this implementation list must be ordered
size = len(data)
objective = 76

def binarySearch(data, left, right, goal):
  while left <= right:
    midPoint = int((right - left) / 2) + left
    if data[midPoint] == goal:
      return midPoint
    if data[midPoint] < goal:
      left = midPoint + 1
    elif data[midPoint] > goal:
      right = midPoint - 1
    else:
      return -1

print("Result of binary search: ", binarySearch(data, 0 , size - 1, objective))
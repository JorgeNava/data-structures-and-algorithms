data = [1,4,76,2,452,23]
size = len(data)
objective = 452

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
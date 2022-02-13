data = [1,4,76,2,452,23]
size = len(data)
objective = 452

def binarySearch(data, left, right, goal):
  if right >= left:
    # Get mid point by getting subarray size then /2 
    # and adding does values to the starting point
    midPoint = int((right - left) / 2) + left 
    if data[midPoint] == goal: # Base case of recursivity
      return midPoint
    elif data[midPoint] > objective: # Search in left side of vector
      return binarySearch(data, left, midPoint - 1, goal)
    elif data[midPoint] < objective: # Search in right side of vector
      return binarySearch(data, midPoint + 1, right, goal)
    else:
      return -1
  else:
    return -1

print("Result of binary search: ", binarySearch(data, 0 , size - 1, objective))
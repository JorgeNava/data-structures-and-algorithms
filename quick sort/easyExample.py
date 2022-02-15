def divide(list):
  pivot = list[0]
  leftSide = []
  rightSide = []
  for i in range(1, len(list)):
    if list[i] >= pivot:
      rightSide.append(list[i])
    else:
      leftSide.append(list[i])
  return leftSide, [pivot], rightSide

def quickSort(list):
  if len(list) < 2:
    return list
  else:
    leftSide, pivot, rightSide = divide(list)
  return quickSort(leftSide) + pivot + quickSort(rightSide)


list = [8, 12, 3, 11, 5, 9, 10, 4, 15, 7]
print(quickSort(list))
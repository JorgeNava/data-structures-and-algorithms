#arr = [3, 4, 1, 6, 2]
arr = [2, 4, 7, 1, 5, 3]
arrSize = len(arr)
output = list() #[6], [6, 2], [1, 6], [4, 1, 6], [3, 4, 1, 6]

for i in range(arrSize):
	actNum = arr[i]
	contiguousArrays = 1 #start per default in one
    
	completeFoundedSubarray = list()
	completeFoundedSubarray.append(actNum)
    
	foundedSubarray = list()
	foundedSubarray.append(actNum)
	for latestTestedIndex in range(i,arrSize):
		rightNum = arr[latestTestedIndex+1] if latestTestedIndex+1 < arrSize else -1
		if rightNum != -1:
			if actNum > rightNum:
				foundedSubarray.append(rightNum)
			else:
				break
		else:
			break
		if len(foundedSubarray) > 1:
			completeFoundedSubarray.append(foundedSubarray)
			contiguousArrays += 1
	
	foundedSubarray = list()
	foundedSubarray.append(actNum)
    # range(i,1)
	for latestTestedIndex in range(0,i):
		leftNum = arr[latestTestedIndex-1]
		if actNum > leftNum:
			foundedSubarray.append(leftNum)
		else:
			break
		if len(foundedSubarray) > 1:
			completeFoundedSubarray.append(foundedSubarray)
			contiguousArrays += 1
    
    
    
    
	output.append(contiguousArrays)
	print("latestTestedIndex: ", latestTestedIndex)
	print("completeFoundedSubarray: ", completeFoundedSubarray)
	print("contiguousArrays: ", contiguousArrays)
	print("-------------------")
print("output: ", output)
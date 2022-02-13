arr = [3, 4, 1, 6, 2] 
realOutput = [1, 3, 1, 5, 1]
#arr = [2, 4, 7, 1, 5, 3] 
#realOutput = [1, 2, 6, 1, 3, 1]
arrSize = len(arr)
output = list() 

contiguousSubArrays = []

	# Prepare for new subarrays
for i in range(arrSize):
	contiguousSubArrays.append({
		"num": arr[i],
		"count": 1,
		"arrays": [[arr[i]]]
	})

j = 0
k = 0
for i in range(arrSize):
	ACT_NUM = arr[i]

	if i+1 < arrSize: #if theres right side
		NEXT_NUM = arr[i+1]
		if ACT_NUM > NEXT_NUM: 
			smaller = i + 1
			bigger = i
			contiguousSubArrays[i]["count"] += 1
			contiguousSubArrays[i]["arrays"].append([NEXT_NUM])
		else:
			smaller = i
			bigger = i + 1
			contiguousSubArrays[i+1]["count"] += 1
			contiguousSubArrays[i+1]["arrays"].append([ACT_NUM])



"""
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
"""
"""
print("latestTestedIndex: ", latestTestedIndex)
print("completeFoundedSubarray: ", completeFoundedSubarray)
print("contiguousArrays: ", contiguousArrays)
print("-------------------")
"""

for i in range(len(contiguousSubArrays)):
	output.append(contiguousSubArrays[i]["count"])
	print("#",i,": ", contiguousSubArrays[i])
	print("========================================")
print("Output: ", output)
print("Output: ", realOutput)
def numberOfWays(numbers, target):
    count = 0
    auxDic = {}
    # iterate through every element of the list
    # get the complementary part of the actual number and store it on an auxilar dictionary
    # then iterate through the array again and count every time a complementary number appears

    

    return count

tests = [
    {   
        "arr": [1, 5, 3, 3, 3],
        "n": 5,
        "k": 6,
        "output": 4
    },
]
for test in tests:
  print("Test list: ", test["arr"])
  print("Obtained result: ", numberOfWays(test["arr"], test["k"]))
  print("Real result: ", test["output"])
  print("TEST RESULT: ", numberOfWays(test["arr"], test["k"]) == test["output"])
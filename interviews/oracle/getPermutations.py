"""
Design a program that could accept words and determine if the
current word is a permutation of a previously submitted word.

A permutation is any arrangement of the same letters in a different
order.

E.g.
User: GOD
Response: GOD: No permutations found
User: DOG
Response: DOG: GOD
User: HELP
Response: HELP: No permutations found
User: PHEL
Response: PHEL: HELP
User: GOO
Response: GOO: No permutations found
User: GDO
Response: GDO: GOD, DOG
"""

permutations = {}

def getPermutations(word):
  sortedWord = ''.join(sorted(word))
  if sortedWord in permutations:
    permutations[sortedWord].append(word)
    return permutations[sortedWord]
  else:
    permutations[sortedWord] = [word]
    return 'No permutations found'

print(getPermutations('GOD'))
print(getPermutations('DOG'))
print(getPermutations('HELP'))
print(getPermutations('PHEL'))
print(getPermutations('GOO'))
print(getPermutations('GDO'))
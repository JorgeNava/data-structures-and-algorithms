#Given a set, return its power set - where the power set is the set of all subsets of the input (or: all sets tha can be constructed using elements in the input set)
# {A, B, C}
# =>
# {
#   { }
#   { A }
#   { B }
#   { C }
#   { A, B }
#   { A, C }
#   { B, C }
#   { A, B, C }
# }

def myAlgo(s):
  subSets = [[]]
  for i in range(len(s)):
    subSets.append([s[i]])
    for j in range(i, len(s)):
      if i != j:
        subSets.append([s[i],s[j]])
  subSets.append(s)
  return subSets

s = ['A', 'B', 'C']
print(myAlgo(s))

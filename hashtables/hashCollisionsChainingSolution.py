#Hash Table class
class HashTable:
  def __init__(self):
    self.MAX = 10
    # Initialize to array to store pair of key and value
    self.arr = [[] for i in range(self.MAX)]

  def get_hash(self, key):
    h = 0
    for char in key:
      h += ord(char)
    return h % self.MAX 

  def __getitem__(self, key): 
    h = self.get_hash(key)
    # Check within the hash index the specific key
    for el in self.arr[h]:
      if el[0] == key:
        return el[1]

  # Now this can override values in hast table elements within the linked list
  def __setitem__(self, key, val):
    h = self.get_hash(key)
    found = False
    
    # Find right location of linked list to override the value
    for i, el in enumerate(self.arr[h]):
      if len(el) == 2 and el[0] == key:
        self.arr[h][i] = (key, val) 
        found = True
        break
    
    # Check if key is already in use
    if not found:
      # Add pair of key and val to linked list
      self.arr[h].append((key, val))

  def __delitem__(self, key): 
    h = self.get_hash(key)
    for i, kv in enumerate(self.arr[h]):
      if kv[0] == key:
        del self.arr[h][i]



t = HashTable()
# They have the same index
print(t.get_hash('march 6')) 
print(t.get_hash('march 17'))

t['march 6'] = 130
t['march 17'] = 140

print(t.arr)
print(t['march 6'])
print(t['march 17'])

del t['march 6']
print('march 6 after being removed: ', t['march 6'])
print(t.arr)

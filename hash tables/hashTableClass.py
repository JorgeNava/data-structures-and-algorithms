"""
  Still missing elements collision handling.
"""
#Hash Table class
class HashTable:
  def __init__(self):
    self.MAX = 100
    self.arr = [None for i in range(self.MAX)]

  # Hash function
  def get_hash(self, key):
    h = 0
    for char in key:
      h += ord(char)
    return h % self.MAX #Not bigger than the array size

  # __setitem__ and __getitem__ makes possible to 
  # just use dict[] to add and get values from keys
  def add(self, key, val):
    h = self.get_hash(key)
    self.arr[h] = val
  def __setitem__(self, key, val):
    h = self.get_hash(key)
    self.arr[h] = val

  def get(self, key): 
    return self.arr[self.get_hash(key)]
  def __getitem__(self, key): 
    return self.arr[self.get_hash(key)]

  def __delitem__(self, key): 
    h = self.get_hash(key)
    self.arr[h] = None

  

t = HashTable()
t.add('march 6', 130) # Adds element to hash table
t['march 7'] = 140 # Adds element to hash table with __setitem__

print(t.get('march 6')) # Gets element by key and hash function
print(t['march 7']) # Gets element by key and hash function with __getitem__

# Notice that elements aren't stored orderd, 
# they're place based in the hash function results
print(t.arr)

del t['march 6']
print('march 6 after being removed: ', t['march 6'])

#Generating collisions in hash table
t['march 18'] = 301 # Collisionates with 'march 7',

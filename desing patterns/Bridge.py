class ProducingAPI1: 
    def produceCuboid(self, length, breadth, height): 
        print(f'API1 is producing Cuboid with length = {length}, '
              f' Breadth = {breadth} and Height = {height}') 
  
class ProducingAPI2: 
    def produceCuboid(self, length, breadth, height): 
        print(f'API2 is producing Cuboid with length = {length}, '
              f' Breadth = {breadth} and Height = {height}') 
  
class Cuboid: 
    def __init__(self, length, breadth, height, producingAPI): 
        self._length = length 
        self._breadth = breadth 
        self._height = height 
        self._producingAPI = producingAPI 
  
    def produce(self): 
        self._producingAPI.produceCuboid(self._length, self._breadth, self._height) 
  
    def expand(self, times): 
        self._length = self._length * times 
        self._breadth = self._breadth * times 
        self._height = self._height * times 
  
cuboid1 = Cuboid(1, 2, 3, ProducingAPI1()) 
cuboid1.produce() 
  
cuboid2 = Cuboid(19, 19, 19, ProducingAPI2()) 
cuboid2.produce() 

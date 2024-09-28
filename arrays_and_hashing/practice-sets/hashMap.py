class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.map = [None] * capacity

    def __str__(self):
        return str(self.map)

    def hash(self, key):
        index = 0
        for c in key:
            index += ord(c)
        return index % self.capacity

        
    def get(self, key: int):
        index = self.hash(key)

        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].value
            index += 1
            index = index % self.capacity
        return None

    def insert(self, key: int, value: int):
        index = self.hash(key)

        while True:
            if self.map[index] == None:
                self.map[index] = Pair(key, value)
                self.size += 1
                if self.size > self.capacity // 2:
                    self.resize()
                return
            elif self.map[index].key == key:
                self.map[index].value = value
                return
            index += 1
            index = index % self.capacity
            
            

    # def remove(self, key: int) -> bool:


    # def getSize(self) -> int:


    # def getCapacity(self) -> int:


    # def resize(self) -> None:



hashMap = HashTable(2)
print(f"Initial hashMap array: {hashMap}")
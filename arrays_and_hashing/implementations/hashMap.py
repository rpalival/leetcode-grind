'''
- array under the hood => [KV, KV, KV] and stores such KV pairs
- we need to figure out at what index to store these KV pairs
- for that we need a way to hash the KV pair (only the key part) and get a integer
- this integer might be out of bounds of our initial hashmap so integer % array.capacity
- now incase multiple keys give us back same index integer, we need to avoid collisions like these
- lot of ways: rehashing, chaining, open addressing, using prime number as array capacity
'''

# simple implementation
'''
Gist:
1. class for key, value pair
2. main hashmap class:
3. initialize the size, capacity and None valued array called map
4. hash(key) -> hashes key and returns integer which can be used as index
Note: always get the index first to perform any sort of operation by using hash()
5. get(key) -> 
    1. get index
    2. in a while loop where index != None:
        1. if at this index.key == key: -> return index.value
        2. if not keep finding at next index+1 and make sure to keep index within capacity (%)
    3. return None
'''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"{self.key}: {self.value}"

class hashMap:
    def __init__(self):
        self.size = 0
        self.capacity = 2
        # under the hood its implemented as array, later on it will be occupied by Pair objects
        self.map = [None] * self.capacity

    def __str__(self):
        result = []
        for item in self.map:
            if item is None:
                result.append("None")
            else:
                result.append("{"+str(item)+"}")
        return "[" + ", ".join(result) + "]"
    
    # our hash method to return index within the capacity limit
    def hash(self, key):
        index = 0
        for c in key:
            index += ord(c)
        return index % self.capacity
    
    # get the value of the key
    def get(self, key):
        index = self.hash(key)

        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].value
            # use chaining method to find the key at nearest location
            index += 1
            # so that our index doesn't go out of bounds
            index = index % self.capacity
        return None
    

    def put(self, key, value):
        index = self.hash(key)

        while True:
            if self.map[index] == None:
                self.map[index] = Pair(key, value)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.rehash()
                return
            elif self.map[index].key == key:
                self.map[index].value = value
                return
            
            index += 1
            index = index % self.capacity

    def remove(self, key):
        if not self.get(key):
            return
        
        index = self.hash(key)
        while True:
            if self.map[index].key == key:
                self.map[index] = None
                self.size -= 1
                return
            index += 1
            index = index % self.capacity

    def rehash(self):
        self.capacity *= 2
        newMap = [None] * self.capacity

        oldMap = self.map
        self.map = newMap
        self.size = 0
        for pair in oldMap:
            if pair:
                self.put(pair.key, pair.value)

    def print(self):
        for pair in self.map:
            if pair:
                print(pair.key, pair.value)




    
hashTable = hashMap()
print(f"Initial hashMap array: {hashTable}")
print("-------------------------------------------------")
hashTable.put("Name", "Raj")
print(f"after insert hashMap array: {hashTable}")
print(f"map array capacity: {hashTable.capacity}")
print(f"map array size: {hashTable.size}")
print("-------------------------------------------------")
print(hashTable.get("Name"))
print("-------------------------------------------------")
hashTable.remove("Name")
print(f"after removing hashMap array: {hashTable}")
print(f"map array capacity: {hashTable.capacity}")
print(f"map array size: {hashTable.size}")
print("-------------------------------------------------")
hashTable.put("Name", "Raj")
hashTable.put("Age", 22)
hashTable.put("Occupation", "student")
print(f"after insert hashMap array: {hashTable}")
print(f"map array capacity: {hashTable.capacity}")
print(f"map array size: {hashTable.size}")
print("-------------------------------------------------")
hashTable.print()
            
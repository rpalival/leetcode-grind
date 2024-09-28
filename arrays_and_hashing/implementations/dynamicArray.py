class DynamicArray:
    '''
    •   append(n): Adds an element to the end, resizing if needed.
	•	resize(): Doubles the capacity and copies existing elements.
	•	get(i): Retrieves the element at index i.
	•	set(i, n): Sets the element at index i to n.
	•	removeLast(): Removes the last element.
	•	size(): Returns the number of elements.
    '''
    # initializing an empty array
    def __init__(self):
        self.capacity = 1
        self.length = 0
        self.arr = [None] * self.capacity

    # overriding the default str constructor such that it prints the contents of the object and not the object memory address
    def __str__(self):
        return str(self.arr)
    
    # resize the current array to implement dynamic arrays
    def resize(self):
        # step 1: double its capacity
        self.capacity *= 2
        # step 2: create new array with this new capacity
        new_arr = [None] * self.capacity

        # step 3: copy the current array elements into new array
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        
        # step 4: declare the new array as the current array
        self.arr = new_arr

    # implement the append logic -> such that a given (n) is added to the END of the array
    def append(self, n):
        if self.length == self.capacity:
            self.resize()

        self.arr[self.length] = n
        self.length += 1

    # remove the last element from the array
    def removeLast(self):
        if self.length > 0:
            self.length -= 1
            # setting the element to None incase python doesn't handle it automatically
            self.arr[self.length] = None
        else:
            raise IndexError("Array is empty")
        
    # get the element at any particular index
    def get(self, index):
        if 0 <= index < self.length:
            return self.arr[index]
        else:
            raise IndexError("Index out of bounds")
        
    # set a particular value at any given index
    def set(self, index, value):
        if 0 <= index < self.length:
            self.arr[index] = value
        else:
            raise IndexError("Index out of bounds")
    
    # return current number of elements in the array
    def size(self):
        return self.length
        

arr = DynamicArray()
print(f"Initial array: {arr}")
print("-------------------------------------------------")
arr.append(10)
print(f"appending: {arr}")
print("-------------------")
arr.append(20)
print(f"appending: {arr}")
print(f"current capacity: {arr.capacity}")
print(f"current length: {arr.length}")
print("-------------------")
arr.append(30)
print(f"appending: {arr}")
print(f"current capacity: {arr.capacity}")
print(f"current length: {arr.length}")
print("-------------------")
arr.removeLast()
print(f"appending: {arr}")
print(f"current capacity: {arr.capacity}")
print(f"current length: {arr.length}")
arr.set(1, 30)
print(f"appending: {arr}")
print(f"current capacity: {arr.capacity}")
print(f"current length: {arr.length}")
print(arr.size())
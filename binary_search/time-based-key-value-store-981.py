class TimeMap:
    def __init__(self):
        self.store = {} # key: list of [value, timestamp]
    
    def set(self, key: str, value:str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
     
    def get(self, key:str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        l, r = 0, len(values)-1
        while l <= r:
            mid = (l+r)//2
            #check if the mid keys time is less than or equal to timestamp
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res
    
obj = TimeMap()
print(obj.set("foo","bar",1))
print(obj.get("foo",1))
print(obj.get("foo",3))
print(obj.set("foo", "bar2", 4))
print(obj.get("foo",4))
print(obj.get("foo",5))
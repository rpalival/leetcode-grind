class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pair = [[p,s] for p,s in zip(position, speed)]
        timeStack = []

        for p,s in sorted(pair)[::-1]:
            timeStack.append((target-p)/s)
            if len(timeStack) >= 2 and timeStack[-1] <= timeStack[-2]:
                timeStack.pop()
        return len(timeStack)


obj = Solution()
target = 12
position = [10, 8, 0, 5, 3]
speed = [2,4,1,1,3]

result = obj.carFleet(target, position, speed)
print(result)
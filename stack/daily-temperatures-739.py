class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = [] #storing pair of temperature, index

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t,i))
        return res
    
obj = Solution()
temperatures = [73,74,75,71,69,72,76,73]
result = obj.dailyTemperatures(temperatures)
print(result)  
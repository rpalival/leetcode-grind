class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        resultDict = {}
        for i, n in enumerate(nums):
            compliment = target - n
            if compliment in resultDict:
                return [resultDict[compliment], i]
            resultDict[n] = i

# test
nums = [2, 7, 11, 15]
target = 9
obj = Solution()
result = obj.twoSum(nums, target)
print(result)
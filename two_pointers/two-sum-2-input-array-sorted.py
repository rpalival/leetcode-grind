class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            if numbers[l] + numbers[r] < target:
                l += 1
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            l, r = l+1, r-1

# test
numbers = [2,7,]
target=9
obj = Solution()
result = obj.twoSum(numbers, target)
print(result)
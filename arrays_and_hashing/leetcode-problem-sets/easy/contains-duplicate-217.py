class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        distinct = set()
        for n in nums:
            if n in distinct:
                return True
            distinct.add(n)
        return False



# O(n) 
# 1st attempt: 40min

# test
nums = [1, 2, 3, 1]
obj = Solution()
result = obj.containsDuplicate(nums)
print(result)
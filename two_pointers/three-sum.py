class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and n == nums[i - 1]:
                continue

            l, r = i+1, len(nums) - 1
            while l < r:
                threeSum = n + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
    
# test
if __name__ == "__main__":
    obj = Solution()

    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = obj.threeSum(nums1)
    expected1 = [[-1, -1, 2], [-1, 0, 1]]
    assert result1 == expected1, f"Test 1 failed: {result1}"
    print(f"Test 1 passed: {result1}")

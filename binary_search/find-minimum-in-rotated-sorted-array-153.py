class Solution:
    def findMin(self, nums: list[int]) -> int:
        
        left, right = 0, len(nums)-1
                
        while left < right:
            mid = (left + right) // 2
                        
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                
        return nums[left]
    

obj = Solution()
nums = [3,4,5,1,2]
result = obj.findMin(nums)
print(result)
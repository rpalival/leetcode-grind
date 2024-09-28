class Solution:
    def maxArea(self, height: list[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
    
if __name__ == "__main__":
    obj = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    result = obj.maxArea(height)
    expected_result = 49

    assert result == expected_result, f"Test failed: {result}"
    print(f"Test passed: {result}")


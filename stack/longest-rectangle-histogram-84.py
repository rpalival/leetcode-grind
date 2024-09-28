class Solution():
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxArea = 0
        stack = [] #store the index, height tuple
        heights.append(0) #to be able to traverse whole of stack

        for i, h in enumerate(heights):
            start =  i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        return maxArea

obj = Solution()
heights = [2,1,5,6,2,3]
result = obj.largestRectangleArea(heights)
print(result)
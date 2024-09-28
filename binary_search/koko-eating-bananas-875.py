import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def can_eat_all(speed):
            return sum(math.ceil(pile / speed) for pile in piles) <= h
        
        left, right = 1, max(piles)
        while left < right:
            mid = (left+right) // 2
            if can_eat_all(mid):
                right = mid
            else:
                left = mid + 1
        
        return left


obj = Solution()
piles = [30,11,23,4,20]
h = 5
result = obj.minEatingSpeed(piles,h)
print(result)

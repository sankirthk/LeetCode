import math 
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            hours = 0

            for pile in piles:
                work = math.ceil(pile/mid)
                hours += work
            
            if hours <= h:
                right = mid
            else:
                left = mid + 1
        
        return left
        
        
if __name__ == "__main__":
    piles = [3,6,7,11]
    h = 8
    solution = Solution()
    print(f"Output is: {solution.minEatingSpeed(piles, h)}")
        

        
        
        
            
            
        
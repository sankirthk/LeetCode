from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)
        length = len(piles)
        totalHours = []
        
        for i in range(1, maxPile + 1):
            rate = i
            hours = 0
            for j in range(length):
                work = math.ceil(piles[j] / rate)
                hours += work
            totalHours.append([rate, hours])

        for i, hours in totalHours:
            if hours <= h:
                return i
            
if __name__ == "__main__":
    piles = [25,10,23,4]
    h = 4
    solution = Solution()
    print(f"Output is: {solution.minEatingSpeed(piles, h)}")
        
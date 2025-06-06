from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0

        left, right = 0, len(height) - 1
        maxArea = 0
        area = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            maxArea = max(maxArea, area)
            if height[left] > height[right]:
                right-=1
            else:
                left +=1
        return maxArea
    
if __name__=="__main__":
    input1 = [8,7,2,1]
    solution = Solution()
    print(f"Input is: {input1}")
    print(f"Output is: {solution.maxArea(input1)}")
    


        
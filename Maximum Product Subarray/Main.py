from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        max_so_far = min_so_far = result = nums[0]
    
        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)
            max_so_far = temp_max
            
            result = max(result, max_so_far)
        return result
            
    
if __name__=="__main__":
    input1 = [-2,3,-4]
    solution = Solution()
    print(f"Input is: {input1}")
    print(f"Output is: {solution.maxProduct(input1)}")
    
             
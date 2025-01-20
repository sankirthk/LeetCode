from itertools import product
from typing import List

class Solution:
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            print(res)
            postfix *= nums[i]
            print(postfix)
        return res
                        
            
# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Basic input
    input1 = [1, 2, 3, 4]
    
    print("Input List:", input1)
    output = solution.productExceptSelf(input1)
    print("Output List:", output)

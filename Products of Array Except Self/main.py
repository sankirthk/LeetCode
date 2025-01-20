from typing import List

class Solution:
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productlist = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    product *= nums[j]
            productlist.append(product)
        return productlist        
            
# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Basic input
    input1 = [1, 2, 3, 4]
    
    print("Input List:", input1)
    output = solution.productExceptSelf(input1)
    print("Output List:", output)

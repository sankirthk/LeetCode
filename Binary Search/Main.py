from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        
        median = len(nums) // 2
        print(median)
        if target == nums[median]:
            return median
        elif target > nums[median]:
            return median + self.search(nums[median:], target)
        else:
            return self.search(nums[:median], target)
        
# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Basic input
    input1 = [2,3,4,5,6,7,8]
    target = 3
    print("Input:", input1)
    print("Output:", solution.search(input1,target))

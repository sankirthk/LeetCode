from itertools import product
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        intMap = {}
        for i in range(len(nums)):
            if nums[i] - 1 not in nums:
                intMap[nums[i]] = nums[i
        print(intMap)
            
# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Basic input
    input1 = [2, 20, 4, 10, 3, 4, 5]
    print("Input List:", input1)
    output = solution.longestConsecutive(input1)
    print("Output List:", output)

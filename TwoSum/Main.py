from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i, num in enumerate(nums):
            complement  = target - num
            if complement in numMap:
                return [numMap[complement], i]
            numMap[num] = i

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Basic input
    input1 = [5,5]
    input2 = 10
    print("Input List:", input1, input2)
    output = solution.twoSum(input1, input2)
    print("Output List:", output)
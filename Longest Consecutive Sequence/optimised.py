from typing import List, Optional 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0
        for num in nums:
            if num - 1 not in num_set:
                i = 1
                while num + i in num_set:
                    i += 1
                max_len = max(max_len, i)
            else:
                continue
        return max_len

if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Basic input
    input1  = [2,20,4,10,3,4,5]
    print("Input:", input1)
    output = solution.longestConsecutive(input1)
    print("Outpt: ", output)
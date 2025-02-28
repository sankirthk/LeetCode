from typing import List, Optional

class Solution:
    def trap(self, height: List[int]) -> int:
        def prefixMax(arr: List[int]) -> List[int]:
            prefix = []
            maxElement = 0
            for i in height:
                maxElement = max(maxElement, i)
                prefix.append(maxElement)
            return prefix
        def suffixMax(arr: List[int]) -> List[int]:
            n: int = len(arr)
            suffix = [0] * n
            maxElement = 0
            for i in range(n-1, -1, -1):
                maxElement = max(maxElement, arr[i])
                suffix[i] = maxElement
            return suffix
        prefixMaxArr = prefixMax(height)
        suffixMaxArr = suffixMax(height)
        totalWater = 0
        for i in range(len(height)):
            totalWater += min(prefixMaxArr[i],suffixMaxArr[i]) - height[i]
        
        return totalWater

if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Basic input
    input1 = [0,2,0,3,1,0,1,3,2,1]
    print("Input List:", input1)
    print("Output:", solution.trap(input1))

        
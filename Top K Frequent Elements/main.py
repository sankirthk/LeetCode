from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num]+= 1
        
        sortedFrequency = sorted(frequency.items(),key=lambda item: item[1], reverse=True)
        
        print(sortedFrequency)
        
        result = []
        for i in range(k):
            result.append(sortedFrequency[i][0])
        return result
        
# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Basic input
    input1 = [1,2,2,3,3,3]
    k = 2
    print("Input List:", input1)
    print("k:", k)
    print("Output:", solution.topKFrequent(input1, k))

    input1 = [7, 7]
    k = 1
    print("Input List:", input1)
    print("k:", k)
    print("Output:", solution.topKFrequent(input1, k))
    
    input1 = [1,1,1,2,2,3]
    k = 2
    print("Input List:", input1)
    print("k:", k)
    print("Output:", solution.topKFrequent(input1, k))
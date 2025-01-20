from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPointer, sellPointer = 0, 1
        profit = 0
        maxProfit = 0

        while sellPointer < len(prices):
            if prices[buyPointer] < prices[sellPointer]:
                profit = prices[sellPointer] - prices[buyPointer]
                maxProfit = max(maxProfit, profit)
            else:
                buyPointer = sellPointer
            sellPointer += 1
        return maxProfit

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Basic input
    input1 = [10,1,5,6,7,1]
    print("Input:", input1)
    output = solution.maxProfit(input1)
    print("Output:", output)

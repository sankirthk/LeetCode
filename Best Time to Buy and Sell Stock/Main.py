from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = None
        sell = None
        buy = None
        for i in range(len(prices)):
            sell = prices[i]
            print(sell)
            j = 0
            while j < i:
                buy = prices[j]
                print(buy)
                if profit == None:
                    profit = sell - buy
                elif sell - buy > profit:
                    profit = sell - buy
                j+= 1
        if profit < 0:
            return 0
        return profit

                
            
        
            
# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Basic input
    input1 = [10,1,5,6,7,1]
    print("Input:", input1)
    output = solution.maxProfit(input1)
    print("Output:", output)


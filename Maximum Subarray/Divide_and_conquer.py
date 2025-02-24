from gettext import find
from typing import List, Optional

class Solution:
    def maxSubArray(self, arr: List[int]) -> List[int]:
        def findMaxSub(arr, left, right):
            if left == right:
                return arr[left]
            
            mid = (left + right) // 2
            
            leftSum = findMaxSub(arr, left, mid)
            rightSum = findMaxSub(arr, mid + 1, right)
            crossingSum = findMaxCrossingSum(arr, left, mid, right)
            
            return max(leftSum, crossingSum, rightSum)
        
        def findMaxCrossingSum(arr, left, mid,  right):
            leftSum = float('-inf')
            tempLeftSum = 0
            for i in range(mid, left -1, -1):
                tempLeftSum += arr[i]
                leftSum = max(leftSum, tempLeftSum)
            
            rightSum = float('-inf')
            tempRightSum = 0
            for i in range(mid+1, right+1):
                tempRightSum += arr[i]
                rightSum = max(rightSum, tempRightSum)
                
            return leftSum + rightSum
        
        return findMaxSub(arr, 0, len(arr)-1)
    
if __name__ == "__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    sol = Solution()
    print(sol.maxSubArray(arr))
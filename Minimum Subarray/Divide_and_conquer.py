from gettext import find
from typing import List, Optional

class Solution:
    def minSubArray(self, arr: List[int]) -> List[int]:
        def findMinSub(arr, left, right):
            if left == right:
                return arr[left], [arr[left]]  # Return both sum and subarray
            
            mid = (left + right) // 2
            
            leftSum, leftSubarray = findMinSub(arr, left, mid)
            rightSum, rightSubarray = findMinSub(arr, mid + 1, right)
            crossingSum, crossingSubarray = findMinCrossingSum(arr, left, mid, right)
            
            # Return the subarray with the minimum absolute sum
            if abs(leftSum) <= abs(rightSum) and abs(leftSum) <= abs(crossingSum):
                return leftSum, leftSubarray
            elif abs(rightSum) <= abs(leftSum) and abs(rightSum) <= abs(crossingSum):
                return rightSum, rightSubarray
            else:
                return crossingSum, crossingSubarray
        
        def findMinCrossingSum(arr, left, mid, right):
            # Find best left subarray sum
            leftSum = float('inf')
            tempSum = 0
            minLeftIndex = mid
            for i in range(mid, left - 1, -1):
                tempSum += arr[i]
                if abs(tempSum) < abs(leftSum):
                    leftSum = tempSum
                    minLeftIndex = i
            
            # Find best right subarray sum
            rightSum = float('inf')
            tempSum = 0
            minRightIndex = mid + 1
            for i in range(mid + 1, right + 1):
                tempSum += arr[i]
                if abs(tempSum) < abs(rightSum):
                    rightSum = tempSum
                    minRightIndex = i
            
            # Return combined sum and subarray
            return leftSum + rightSum, arr[minLeftIndex:minRightIndex + 1]
        
        _, resultSubarray = findMinSub(arr, 0, len(arr) - 1)
        return resultSubarray
    
if __name__ == "__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    sol = Solution()
    print(sol.minSubArray(arr))
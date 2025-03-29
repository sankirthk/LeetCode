from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
    
        # If array is not rotated or has only one element
        if nums[left] < nums[right] or left == right:
            return nums[left]
        
        while left < right:
            # Find the middle index
            mid = (right + left) // 2
            
            # If mid element is greater than right element,
            # minimum must be in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            # If mid element is less than or equal to right element,
            # minimum must be in the left half including mid
            else:
                right = mid
        
        # At this point, left == right and points to the minimum element
        return nums[left]


if __name__ == "__main__":
    nums = [3,4,5,6,1,2]
    solution = Solution()
    print(f"Output is: {solution.findMin(nums)}")
        

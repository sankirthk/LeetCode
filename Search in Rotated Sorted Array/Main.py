from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            if nums[left] <= nums[mid]:
                if  nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Basic input
    nums = [3,4,5,6,1,2]
    target = 4
    solution = Solution()
    print(f"Output is: {solution.search(nums, target)}")
from typing import List, Optional 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = self.merge_sort(nums)
        i = 0
        result = []
        while i < len(sorted_nums):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                i += 1
                continue
            target = - sorted_nums[i]
            j = i + 1
            k = len(sorted_nums) - 1
            while j < k:
                if sorted_nums[j] + sorted_nums[k] == target:
                    result.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                    while j < k and sorted_nums[j] == sorted_nums[j + 1]:
                        j += 1
                    while j < k and sorted_nums[k] == sorted_nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif sorted_nums[j] + sorted_nums[k] < target:
                    j += 1
                else:
                    k -= 1
            i += 1
        return result

    

    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])

        return self.merge(left, right)

    def merge(self, left_half, right_half):
        sorted_arr = []
        i, j = 0, 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                sorted_arr.append(left_half[i])
                i += 1
            else:
                sorted_arr.append(right_half[j])
                j += 1
            
        sorted_arr.extend(left_half[i:])
        sorted_arr.extend(right_half[j:])

        return sorted_arr

if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Basic input
    input1  = [-1,0,1,2,-1,-4]
    print("Input:", input1)
    output = solution.threeSum(input1)
    print("Outpt: ", output)
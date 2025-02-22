from typing import List, Optional

class Solution:
    def quickSort(self, arr: List[int], low:int, high:int) -> List[int]:
        if low < high:
            pivotIndex = self.hoarePartition(arr, low, high)
            self.quickSort(arr, low, pivotIndex)
            self.quickSort(arr, pivotIndex + 1, high)
        
        return arr

    def hoarePartition(self, arr: List[int], low:int, high:int) -> int:
        pivot = arr[low]
        i = low - 1
        j = high + 1

        while True:

            i += 1
            while arr[i] < pivot:
                i += 1
            
            j -= 1
            while arr[j] > pivot:
                j -= 1
            
            if i >= j:
                return j
            
            arr[i], arr[j] = arr[j], arr[i]

if __name__ == "__main__":
    solution = Solution()
    input = [14, 12, 14, 19, 5, 3, 4, 14, 7, 22, 16]
    print(solution.quickSort(input, 0, len(input) - 1))
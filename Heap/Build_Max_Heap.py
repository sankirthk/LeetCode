from typing import List, Optional

class Solution:
    def buildMaxHeap(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n//2 - 1, -1, -1):
            self.maxHeapify(arr, n, i)
        return arr
    
    def maxHeapify(self, arr: List[int], n:int, i:int) -> None:
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r

        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]
            self.maxHeapify(arr, n, largest)
    
    def maxHeapExtract(self, arr: List[int]) -> Optional[int]:
        n = len(arr)
        if n == 0:
            return -1
        
        arr[0], arr[n-1] = arr[n-1], arr[0]
        maxElement = arr[n-1]
        arr.pop()
        n -= 1
        self.maxHeapify(arr, n, 0)
        
        return maxElement

if __name__ == "__main__":
    solution = Solution()
    input = [3, 9, 5, 8, 15, 7, 4, 10, 6, 12, 16]
    print(solution.buildMaxHeap(input))
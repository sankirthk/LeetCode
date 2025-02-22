from typing import List, Optional
from Build_Max_Heap import Solution as bh


if __name__ == "__main__":
    test = bh()
    input = [3, 9, 5, 8, 15, 7, 4, 10, 6, 12, 16]
    heap = test.buildMaxHeap(input)
    maxElement, newHeap = test.maxHeapExtract(heap)
    newHeap2 = test.maxHeapInsert(newHeap, 11, len(newHeap))
    print(newHeap2)    
        
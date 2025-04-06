from typing import List
from math import sqrt
import heapq

class Solution:
    def euclideanDistance(self, point: List[int]) -> int:
        distance = sqrt((point[0]**2) + (point[1]**2))
        return distance

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        output = []
        for point in points:
            dist = self.euclideanDistance(point)
            heapq.heappush(heap, (-dist, point))
            if len(heap) > k:
                heapq.heappop(heap)

        return [point for _, point in heap]

if __name__ == "__main__":
    solution = Solution()
    points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
    k = 2
    result = solution.kClosest(points, k)
    print("The", k, "closest points to the origin are:", result)

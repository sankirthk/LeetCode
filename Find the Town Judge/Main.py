from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        adjacencyMatrix = [[0 for i in range(n)] for j in range(n)]
        print(adjacencyMatrix)
        
if __name__ == "__main__":
    input1 = [[1,2],[2,3]]
    n = 3
    solution = Solution()
    print(f"Output is: {solution.findJudge(n, input1)}")

        
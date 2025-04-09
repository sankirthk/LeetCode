from collections import Counter, deque
from typing import List
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        maxHeap = [-x for x in cnt.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            time += 1

            if maxHeap:
                val = 1 + heapq.heappop(maxHeap)
                if val:
                    q.append([val, time + n])
            else:
                time = q[0][1]
                 
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time 

if __name__ == "__main__":

    tasks = ["X","X","Y","Y"]
    n = 2
    solution = Solution()
    print(f"Outptut is: {solution.leastInterval(tasks, n)}")


        
        
        

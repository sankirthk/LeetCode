from typing import List, Optional 
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def from_list(values: List[Optional[int]]) -> Optional['TreeNode']:
        if not values:
            return None

        root = TreeNode(values[0])
        queue = deque([root])
        i = 1

        while queue and i < len(values):
            current = queue.popleft()

            if values[i] is not None:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i += 1

            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            i += 1

        return root

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.diameter = 0

        def dfs(curr):

            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.diameter = max(self.diameter, right + left)

            return 1 + max(left, right)
        
        dfs(root)

        return self.diameter


if __name__ == "__main__":
    values = [1,2,3,4,5,6,7,8]
    bt = TreeNode.from_list(values)
    solution = Solution()
    print(f"Output is: {solution.diameterOfBinaryTree(bt)}")


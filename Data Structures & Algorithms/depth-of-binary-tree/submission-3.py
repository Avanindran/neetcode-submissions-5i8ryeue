# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #recursive sol

        if not root:
            return 0
        q = deque([(root, 1)])
        curr_max_depth = 0
        while q:

            pair = q.popleft()
            node = pair[0]
            depth = pair[1]
            curr_max_depth = max(depth, curr_max_depth)

            if node.left:
                q.append((node.left, depth + 1))

            if node.right:
                q.append((node.right, depth + 1))
        
        return curr_max_depth




        

        


        
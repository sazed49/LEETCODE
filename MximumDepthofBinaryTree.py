# Definition for a binary tree node.
from typing import Optional

import null


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l=self.maxDepth(root.left)
        r=self.maxDepth(root.right)
       # print(l,r)
        return max(l,r)+1
solution = Solution()
root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.left.left=TreeNode(null)
root.left.right=TreeNode(null)
root.right=TreeNode(15)
root.right.left=TreeNode(7)

ans=solution.maxDepth(root)
print(ans)


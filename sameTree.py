# Definition for a binary tree node.
from typing import Optional

import null


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True #both null, so true
        if not p or not q:
            return False  #one null,other not null.so false
        if p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right))
            



solution = Solution()

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
q=TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

ans = solution.isSameTree(p,q)
print(ans)
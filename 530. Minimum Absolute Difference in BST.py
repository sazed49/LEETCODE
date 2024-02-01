# Definition for a binary tree node.
from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev=None
        ans=float("inf")
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nonlocal prev,ans
            if prev:
                ans = min(ans, node.val - prev.val)
                if ans==1:
                    return  ans
                #print("ans--",ans)
            prev=node
            #print("prev--",prev.val)
            dfs(node.right)
        dfs(root)
        return ans



s = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.right =TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
ans = s.getMinimumDifference(root)
print(ans)

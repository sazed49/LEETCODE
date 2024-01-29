# Definition for a binary tree node.
from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        def dfs(node, currentsum)->bool:
            if not node.left and not node.right:
                return currentsum+node.val==targetSum

            left=dfs(node.left, currentsum+node.val) if  node.left else False
            right=dfs(node.right, currentsum+node.val) if node.right else False
            return left or right





        return dfs(root, 0)



solu = Solution()
root = TreeNode(5)
root.left =TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
ans=solu.hasPathSum(root,20)
print(ans)
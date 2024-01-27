# Definition for a binary tree node.
from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return


        #swap child
        tmp=root.left
        root.left=root.right
        root.right=tmp

        self.invertTree(root.left)

        self.invertTree(root.right)

        return root

# Example usage:
# Creating a simple tree
s = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
ans = s.invertTree(root)
print(ans)




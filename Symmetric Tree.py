from typing import Optional  #Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    flag=True
    def dfs(self, leftNode: Optional[TreeNode],rightNode: Optional[TreeNode]) -> None:
            if leftNode is None and rightNode is None:
                return True
            elif leftNode is None or rightNode is  None:
                self.flag=False
                return False
            if (leftNode.val!= rightNode.val):
                self.flag=False
                return False
            self.dfs(leftNode.left,rightNode.right)
            self.dfs(leftNode.right,rightNode.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:


        self.dfs(root.left,root.right)
        return self.flag




sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(None)
root.left.right = TreeNode(3)
root.right.left = TreeNode(None)
root.right.right = TreeNode(3)
ans=sol.isSymmetric(root)
print(ans)

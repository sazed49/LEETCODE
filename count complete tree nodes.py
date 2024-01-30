# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leftheight(self, root) -> int:
        if not root:
            return 0
        return self.leftheight(root.left) + 1

    def rightheight(self, root) -> int:
        if not root:
            return 0
        return self.rightheight(root.right) + 1

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0;
        lh = self.leftheight(root)
        rh = self.rightheight(root)

        if lh == rh:
            return pow(2, lh) - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1



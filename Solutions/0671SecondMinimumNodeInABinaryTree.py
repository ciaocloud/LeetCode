from typing import Optional

from Solutions.utils import TreeNode


def findSecondMinimumValue(root: Optional[TreeNode]) -> int:
    inorder = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        inorder.append(node.val)
        dfs(node.right)
from Solutions.utils import TreeNode


def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    def dfs(node):
        if not node:
            return 0, 0
        leftDepth, leftMax = dfs(node.left, diameter)
        rightDepth, rightMax = dfs(node.right, diameter)
        diameter = max(leftDepth + rightDepth, leftMax, rightMax)
        return 1 + max(leftDepth, rightDepth), diameter
    return dfs(root, 0)[1]

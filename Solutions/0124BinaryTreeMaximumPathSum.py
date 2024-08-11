from Solutions.utils import TreeNode


def maxPathSum(root: TreeNode) -> int:
    ans = [-math.inf]

    def dfs(node: TreeNode) -> int:
        ## maxgain
        if not node:
            return 0
        leftgain = max(0, dfs(node.left))
        rightgain = max(0, dfs(node.right))
        ans[0] = max(ans[0], leftgain+rightgain+node.val)
        return max(leftgain, rightgain) + root.val

    return dfs(root)[0]
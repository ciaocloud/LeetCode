class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rob(root: Optional[TreeNode]) -> int:
    def robTree(node):
        ## [rob current, don't rob current]
        if not node:
            return 0, 0
        left = robTree(node.left)
        right = robTree(node.right)
        robCurrent = node.val + left[1] + right[1]
        doNotRobCurrent = max(left) + max(right)
        return robCurrent, doNotRobCurrent

    return max(robTree(root))

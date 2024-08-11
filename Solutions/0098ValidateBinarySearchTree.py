import math

from Solutions.utils import TreeNode


def isValidBST(root: Optional[TreeNode]) -> bool:
    def validate(node, low, high):
        if node is None:
            return True
        if node.val <= low or node.val >= high:
            return False
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)
    return validate(root, -math.inf, math.inf)

def isValidBstIter(root: Optional[TreeNode]) -> bool:
    stack = []
    if root:
        stack.append((root, -math.inf, math.inf))
    while stack:
        node, low, high = stack.pop()
        if node.val <= low or node.val >= high:
            return False
        if node.left:
            stack.append((node.left, low, node.val))
        if node.right:
            stack.append((node.right, node.val, high))
    return True
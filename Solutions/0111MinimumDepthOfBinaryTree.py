import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# def constructBinaryTree(nodeVals):
#     if not nodeVals:
#         return None
#     nodes = collections.deque()
#     for val in nodeVals:
#         node = None
#         if val is not None:
#             node = TreeNode(val)
#         nodes.append(node)
#     i = 0
#     while i < len(nodes):
#         cur = nodes[i]


def minDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    if not root.left:
        return 1 + minDepth(root.right)
    if not root.right:
        return 1 + minDepth(root.left)
    return 1 + min(minDepth(root.left), minDepth(root.right))

def minDepthBSF(root: Optional[TreeNode]) -> int:
    queue = collections.deque()
    level = 0
    if root:
        queue.append(root)
    while queue:
        level += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if not node.left and not node.right:
                return level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return level


if __name__ == '__main__':
    pass

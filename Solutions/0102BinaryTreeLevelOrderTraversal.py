import collections
from typing import List, Optional

from Solutions.utils import TreeNode


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    ans = []
    queue = collections.deque()
    if root:
        queue.append(root)
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        ans.append(level)
    return ans

def levelOrderIterative(root: Optional[TreeNode]) -> List[List[int]]:
    ans = []
    def dfs(level, node):
        if level == len(ans):
            ans.append([])
        ans[level].append(node.val)
        if node.left:
            dfs(level + 1, node.left)
        if node.right:
            dfs(level + 1, node.right)
    if root:
        dfs(0, root)
    return ans


if __name__ == '__main__':
    pass
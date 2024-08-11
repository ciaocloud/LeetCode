from typing import Optional

from Solutions.utils import TreeNode


def connect(root: Optional[TreeNode]) -> Optional[TreeNode]:
    leftmost = root
    while leftmost and leftmost.left:
        cur = leftmost
        while cur:
            ## Use the fact of PERFECT BINARY TREE
            ## Case # 1: left child points to right child
            cur.left.next = cur.right
            ## Case #2: right child points to adjacent left child
            if cur.next:
                cur.right.next = cur.next.left
            ## Iterate for this level
            cur = cur.next
        ## go to the next level
        leftmost = leftmost.left
    return root

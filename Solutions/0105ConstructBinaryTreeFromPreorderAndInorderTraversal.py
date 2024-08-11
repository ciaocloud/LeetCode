from typing import List, Optional

from Solutions.utils import TreeNode


def buildTreeSimple(preorder: List[int], inorder: List[int]) -> Optinal[TreeNode]:
    if not preorder or not inorder:
        return None
    val = preorder[0]
    root = TreeNode(val)
    i = inorder.index(val)
    root.left = buildTreeSimple(preorder[1:i+1], inorder[:i])
    root.right = buildTreeSimple(preorder[i+1:], inorder[i+1:])
    return root

def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
    imap = {}
    for i, v in enumerate(inorder):
        imap[v] = i

    def build(pl, pr, il, ir):
        if pl > pr:
            return None
        val = preorder[pl]
        root = TreeNode(val)
        i = imap[val]
        leftsize = i - il
        root.left = build(pl+1, pl+leftsize, il, i-1)
        root.right = build(pl+leftsize+1, pr, i+1, ir)
        return root

    return build(0, len(inorder)-1, 0, len(inorder)-1)
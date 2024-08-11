from typing import Optional

from Solutions.utils import TreeNode


def isSubtree(root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
    def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        if not isSameTree(p.left, q.left) or not isSameTree(p, q.right):
            return False
        return True

    if isSameTree(root, subroot):
        return True
    if not root:
        return False
    ## For each of the N nodes in the tree, we check isSameTree (which takes O(M) time where M = subtree size).
    ## Thus the overall time complexity is O(MN).
    return isSubtree(root.left, subroot) or isSubtree(root.right, subroot)

    self.preorder, self.inorder = preorder, inorder
    self.indices = dict()
    for i, v in enumerate(inorder):
        self.indices[v] = i

    return self.build(0, len(preorder) - 1, 0, len(inorder) - 1)


def build(self, preLo, preHi, inLo, inHi):
    if preLo > preHi:
        # if inLo > inHi:
        return None
    val = self.preorder[preLo]
    root = TreeNode(val)
    # m = inLo
    # for i in range(inLo, inHi):
    #     if self.inorder[i] == val:
    #         m = i
    #         break
    m = self.indices[val]
    leftlen = m - inLo
    root.left = self.build(preLo + 1, preLo + leftlen, inLo, m - 1)
    root.right = self.build(preLo + leftlen + 1, preHi, m + 1, inHi)
    return root
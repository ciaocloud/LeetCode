from Solutions.utils import TreeNode


def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root:
        return None
    if root.val > p.val and root.val > q.val:
        return lowestCommonAncestor(root.left, p, q)
    if root.val < p.val and root.val < q.val:
        return lowestCommonAncestor(root.right, p, q)
    return root

def lca(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    while root:
        if root.val > p.val and root.val > q.val:
            root = root.left
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            return root
    return None

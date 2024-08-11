from Solutions.utils import TreeNode


def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    def dfs(root, p, q):
        if not root:
            return None, 0
        found = 0
        if root == p:
            found += 1
        if root == q:
            found += 1
        left = dfs(root.left, p, q)
        if left[0]:
            return left
        found += left[1]
        right = dfs(root.right, p, q)
        if right[0]:
            return right
        found += right[1]
        if found == 2:
            return root, 2
        return None, found

    return dfs(root, p, q)[0]

def helper(self, root, p, q):
    lca, foundp, foundq = None, False, False
    if not root:
        return (lca, foundp, foundq)
    left = self.helper(root.left, p, q)
    if left[0]:
        return left
    right = self.helper(root.right, p, q)
    if right[0]:
        return right
    foundp = left[1] or right[1]
    foundq = left[2] or right[2]
    if root == p:
        foundp = True
    if root == q:
        foundq = True
    if foundp and foundq:
        return (root, foundp, foundq)
    return (None, foundp, foundq)
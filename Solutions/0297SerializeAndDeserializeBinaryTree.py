from collections import deque

from Solutions.utils import TreeNode


class Codec:
    def serialize(self, root:TreeNode) -> str:
        """Encodes a tree to a single string."""
        sb = []
        def preorder(node):
            if not node:
                sb.append('#,')
            sb.append(str(node.val) + ',')
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ''.join(sb)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        queue = deque(data.split(','))

        def build(queue):
            val = queue.popleft()
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = build(queue)
            node.right = build(queue)
            return node

        return build(queue)


if __name__ == '__main__':
    codec = Codec()
    root = codec.deserialize('[1,2,3]')
    ans = codec.deserialize(codec.serialize(root))
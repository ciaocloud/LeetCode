class Node:
    def __init__(self, val: int = 0, left: "Node" = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root: Node) -> Node:
    leftmost = root

    def process(child, ):
        if not child:
            return
        if prev:
            prev.next = child
        else:
            leftmost = child
        prev = child

    while leftmost:
        p, q = leftmost, None ## the current node in this level and the next level
        leftmost = None
        while p:
            if p.left:
                if not q:
                    leftmost = p.left
                else:
                    q.next = p.left
                q = p.left
            if p.right:
                if not q:
                    leftmost = p.right
                else:
                    q.next = p.right
                q = p.right
            p = p.next

            # process(p.right)
            # p = p.next
    return root

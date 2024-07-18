from collections import deque
from typing import Optional

class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraphDfs(node: Optional['Node']) -> Optional['Node']:
    if node is None:
        return None
    mapping = dict()
    def dfs(u):
        if u in mapping:
            return
        ucopy = Node(u.val)
        mapping[u] = ucopy
        neighbors = []
        for v in u.neighbors:
            dfs(v)
            vcopy = mapping[v]
            neighbors.append(vcopy)
        ucopy.neighbors = neighbors

    dfs(node)
    return mapping[node] if node in mapping else None

def cloneGraphBfs(node: Optional['Node']) -> Optional['Node']:
    if node is None:
        return None
    mapping = dict()
    queue = deque([node])
    while queue:
        u = queue.popleft()
        if not u in mapping:
            mapping[u] = Node(u.val)
        ucopy = mapping[u]
        neighbors = []
        for v in u.neighbors:
            if v not in mapping:
                mapping[v] = Node(v.val)
                queue.append(v)
            vcopy = mapping[v]
            neighbors.append(vcopy)
        ucopy.neighbors = neighbors
    return mapping[node] if node in mapping else None

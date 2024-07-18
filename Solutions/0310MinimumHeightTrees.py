import collections
from typing import List


def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]:
    nodes = set(range(n))
    graph = collections.defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    leaves = collections.deque()
    for v in graph:
        if len(graph[v]) == 1:
            leaves.append(v)
    # while len(graph) > 2:
    while len(nodes) > 2:
        for _ in range(len(leaves)):
            u = leaves.popleft()
            for v in graph[u]:
                graph[v].remove(u)
                if len(graph[v]) == 1:
                    leaves.append(v)
            # del graph[u]
            nodes.remove(u)
    return list(nodes)

if __name__ == '__main__':
    n = 1
    edges = []
    print(findMinHeightTrees(n, edges))
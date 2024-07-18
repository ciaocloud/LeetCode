from collections import defaultdict, deque
from typing import List


def validPathDfs(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = set()
    def dfs(u: int, visited: set) -> bool:
        if u == destination:
            return True
        visited.add(u)
        for v in graph[u]:
            if v not in visited and dfs(v, visited):
                return True
        return False
    return dfs(source, visited)

def validPathDfsStack(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * n
    stack = [source]
    while stack:
        u = stack.pop()
        visited[source] = True
        if u == destination:
            return True
        for v in graph[u]:
            if not visited[v]:
                stack.append(v)
    return False

def validPathBfs(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * n
    queue = deque()
    queue.append(source)
    while queue:
        u = queue.popleft()
        if u == destination:
            return True
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                queue.append(v)
    return False

def validPathUnionFind(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    parent = [i for i in range(n)]
    size = [1] * n

    def find(v):
        if v != parent[v]:
            parent[v] = find(parent[v])
        return parent[v]

    def union(u, v):
        uroot = find(u)
        vroot = find(v)
        if uroot == vroot:
            return
        if size[uroot] < size[vroot]:
            parent[uroot] = vroot
            size[uroot] += size[vroot]
        else:
            parent[vroot] = uroot
            size[vroot] += size[uroot]

    for u, v in edges:
        union(u, v)

    return find(source) == find(destination)


if __name__ == '__main__':
    n = 3
    edges = [[0,1],[1,2],[2,0]]
    source = 0
    destination = 2
    print(validPathDfs(n, edges, source, destination))
    print(validPathBfs(n, edges, source, destination))
    print(validPathUnionFind(n, edges, source, destination))

    n = 6
    edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
    source = 0
    destination = 5
    print(validPathDfs(n, edges, source, destination))
    print(validPathBfs(n, edges, source, destination))
    print(validPathUnionFind(n, edges, source, destination))

import collections
from typing import List


def calEquationUf(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    # parent = collections.defaultdict(list)
    # rank = collections.defaultdict(int)
    # weight = collections.defaultdict(float)

    parent, rank, weight = {}, {}, {}

    def find(x):
        if x not in weight:
            weight[x] = 1.0
            parent[x] = x
            rank[x] = 1
        if x != parent[x]:
            px, wx = find(parent[x])
            parent[x] = px
            weight[x] *= wx
        return parent[x], weight[x]

    def union(x, y, z):
        xroot, xweight = find(x)
        yroot, yweight = find(y)
        if xroot == yroot:
            return
        # parent[xroot] = yroot
        # weight[xroot] = yweight * z / xweight

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
            weight[xroot] = yweight * z / xweight
        else:
            parent[yroot] = xroot
            weight[yroot] = xweight / (yweight * z)
            if rank[xroot] == rank[yroot]:
                rank[xroot] += 1

    for (x, y), z in zip(equations, values):
        union(x, y, z)

    ans = []
    for x, y in queries:
        if not x in weight or not y in weight:
            ans.append(-1.0)
        else:
            xroot, xweight = find(x)
            yroot, yweight = find(y)
            if xroot != yroot:
                ans.append(-1.0)
            else:
                ans.append(xweight / yweight)
    return ans

def calEquationDfs(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    graph = collections.defaultdict(list)
    for (x, y), z in zip(equations, values):
        graph[x].append((y, z))
        graph[y].append((x, 1.0/z))

    def dfs(u, dst, visited, i):
        if u == dst:
            return True
        visited.add(u)
        for v, z in graph[u]:
            if not v in visited:
                if dfs(v, dst, visited, i):
                    # self.res *= z
                    ans[i] *= z
                    return True
        return False

    ans = [-1.0] * len(queries)
    for i, (x, y) in enumerate(queries):
        if x not in graph or y not in graph:
            continue
        visited = set()
        ans[i] = 1.0
        if not dfs(x, y, visited, i):
            ans[i] = -1.0
    return ans


if __name__ == '__main__':
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(calEquationUf(equations, values, queries))
    print(calEquationDfs(equations, values, queries))

    equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
    values = [1.5, 2.5, 5.0]
    queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
    print(calEquationUf(equations, values, queries))
    print(calEquationDfs(equations, values, queries))
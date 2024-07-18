import collections
from typing import List


def minimumSemestersDfs(n: int, relations: List[List[int]]) -> int:
    graph = collections.defaultdict(list)
    for u, v in relations:
        graph[u].append(v)

    color = [0] * (n+1)
    def dfs(u):
        if color[u] != 0:
            return color[u]
        color[u] = -1
        height = 1
        for v in graph[u]:
            if color[v] == -1:
                return -1
            elif color[v] == 0 and dfs(v) == -1:
                return -1
            else:
                height = max(height, dfs(v)+1)
            # heightV = dfs(v)
            # if heightV == -1:
            #     return -1
            # height = max(height, heightV + 1)
        color[u] = height
        return height

    ans = 0
    for v in range(1, n+1):
        height = dfs(u)
        if height == -1:
            return height
        ans = max(ans, height)
    return ans

if __name__ == '__main__':
    n = 3
    relations = [[1,3],[2,3]]
    print(minimumSemestersDfs(n, relations))
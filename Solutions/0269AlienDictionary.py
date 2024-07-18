import collections
from typing import List


def alienOrderDfsTopoSort(words: List[str]) -> str:
    graph, color = {}, {}
    for word in words:
        for c in word:
            graph[c] = set()
            color[c] = 0
    for i in range(1, len(words)):
        w1, w2 = words[i-1], words[i]
        for j in range(max(len(w1), len(w2))):
            if j == len(w1) and j < len(w2):
                break
            if j == len(w2) and j < len(w1):
                return ""
            u, v = w1[j], w2[j]
            if u != v:
                graph[u].add(v)
                break

    postorder = []
    def dfs(u):
        color[u] = -1
        for v in graph[u]:
            if color[v] == -1:
                return True
            elif color[v] == 0 and dfs(v):
                return True
        color[u] = 1
        postorder.append(u)
        return False

    for v in graph:
        if color[v] == 0 and dfs(v):
            return ""
    return "".join(postorder[::-1])

def alienOrderBfsTopoSort(words: List[str]) -> str:
    


if __name__ == '__main__':
    # print(alienOrder(["eat", "tea", "ate", "nat", "bat"]))
    print(alienOrder(["wrt","wrf","er","ett","rftt"]))
    # print(alienOrder(["ac","ab","zc","zb"]))

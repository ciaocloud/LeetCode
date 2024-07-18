from typing import List


def allPathsFromSourceToTarget(graph: List[List[int]]) -> List[List[int]]:
    allPaths = []
    visited = set([0])
    # visited.add(0)
    backtrack([0], graph, visited, len(graph)-1, allPaths)
    return allPaths

def backtrack(path, graph, visited, target, allPaths):
    u = path[-1]
    if u == target:
        allPaths.append(path[:])
        return
    for v in graph[u]:
        if v not in visited:
            path.append(v)
            visited.add(v)
            backtrack(path, graph, visited, target, allPaths)
            visited.remove(v)
            path.pop()

if __name__ == '__main__':
    graph = [[1,2],[3],[3],[]]
    print(allPathsFromSourceToTarget(graph))

    graph = [[4,3,1],[3,2,4],[3],[4],[]]
    print(allPathsFromSourceToTarget(graph))
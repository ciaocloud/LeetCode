import collections
from typing import List


def numIslandsDfs(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0
    m, n = len(grid), len(grid[0])
    # visited = [[False] * n for _ in range(m)]
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    ans = 0
    def dfs(x, y):
        # visited[x][y] = True
        grid[x][y] = '#'
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if grid[nx][ny] == '1': # and not visited[nx][ny]:
                dfs(nx, ny)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1': # and not visited[i][j]:
                dfs(i, j)
                ans += 1
    return ans

def numIslandsBfs(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0
    m, n = len(grid), len(grid[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    ans = 0
    queue = collections.deque()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                queue.append((i, j))
                while queue:
                    x, y = queue.popleft()
                    if not grid[x][y] == '1': continue
                    grid[x][y] = '#'
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if nx < 0 or nx >= m or ny < 0 or ny >= n:
                            continue
                        if grid[nx][ny] == '1':
                            queue.append((nx, ny))
                ans += 1
    return ans

if __name__ == '__main__':
    print(numIslandsDfs([]))
    print(numIslandsDfs([["0","1","0"],["1","0","1"],["0","1","0"]]))

    print(numIslandsBfs([]))
    print(numIslandsBfs([["0","1","0"],["1","0","1"],["0","1","0"]]))
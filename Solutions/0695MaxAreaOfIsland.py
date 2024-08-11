import collections
from typing import List


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    ans = 0
    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]
    def dfs(i, j):
        area = 0
        visited[i][j] = True
        # grid[i][j] = -1
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1 and not visited[ni][nj]:
                area += dfs(ni, nj)
        area += 1
        return area

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and not visited[i][j]:
                ans = max(ans, dfs(i, j))
    return ans

def maxAreaOfIslandIterative(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]
    ans = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and not visited[i][j]:
                area = 0
                # stack = []
                # stack.append((i, j))
                queue = collections.deque()
                queue.append((i, j))
                visited[i][j] = True
                # while stack:
                while queue:
                    # r, c = stack.pop()
                    r, c = queue.popleft()
                    area += 1
                    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        nr, nc = r + dr, c + dc
                        if nr >= 0 and nr < m and nc >= 0 and nc < n and grid[nr][nc] == 1 and not visited[nr][nc]:
                            # stack.append((nr, nc))
                            queue.append((nr, nc))
                            visited[nr][nc] = True
                ans = max(ans, area)
    return ans


if __name__ == '__main__':
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(maxAreaOfIslandIterative(grid))
    print(maxAreaOfIsland(grid))

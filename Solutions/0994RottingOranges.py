import collections
from typing import List

def orangesRotting(grid: List[List[int]]) -> int:
    ans = 0
    queue = collections.deque()
    rotten = set()
    def getIndex(i, j):
        return i * len(grid[0]) + j

    fresh = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 2:
                queue.append((x, y, 0))
                rotten.add(getIndex(x, y))
            elif grid[x][y] == 1:
                fresh += 1
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while queue:
        for _ in range(len(queue)):
            x, y, t = queue.popleft()
            ans = max(ans, t)
            for dx, dy in dirs:
                xx, yy = x+dx, y+dy
                if xx >= 0 and xx < len(grid) and yy >= 0 and yy < len(grid[0]):
                    if grid[xx][yy] == 1 and not xx * len(grid[0]) + yy in rotten:
                        # grid[xx][yy] = 2
                        queue.append((xx, yy, t+1))
                        rotten.add(getIndex(xx, yy))
                        fresh -= 1
                        # dt = 1
        # print(t, rotten)
        # t += dt
    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         if grid[i][j] == 1 and (i, j) not in rotten:
    #             return -1
    # return t

    return ans if fresh == 0 else -1

if __name__ == '__main__':
    print(orangesRotting([[0, 0, 0], [0, 0, 1], [0, 0, 2]]))
    print(orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
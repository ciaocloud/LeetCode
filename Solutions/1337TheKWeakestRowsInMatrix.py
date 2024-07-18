from typing import List


def KWeakestRowsInMatrix(matrix: List[List[int]], k: int) -> List[int]:
    ans = []
    m, n = len(matrix), len(matrix[0])
    # for j in reversed(range(n)):
    for j in range(n):
        for i in range(m):
            if i in set(ans):
                continue
            if matrix[i][j] == 0:
                ans.append(i)
                if len(ans) == k:
                    return ans
                break
    for i in range(m):
        if matrix[i][n-1] == 1:
            ans.append(i)
            if len(ans) == k:
                return ans
    return ans

if __name__ == '__main__':
    print(KWeakestRowsInMatrix([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 3))
    print(KWeakestRowsInMatrix([[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]], 1))
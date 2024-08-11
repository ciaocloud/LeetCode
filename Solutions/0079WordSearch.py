from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    m, n = len(board), len(board[0])

    def dfs(i, j, k):
        if k == len(word):
            return True
        if i < 0 or i >= m or j < 0 or j >= n:
            return False
        if board[i][j] != word[k]:
            return False
        board[i][j] = '#'
        for di, dj in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            if dfs(i + di, j + dj, k + 1):
                return True
        board[i][j] = word[k]
        return False

    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0):
                return True
    return False

if __name__ == '__main__':
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    print(exist(board, "ABCCED"))
    print(exist(board, "SEE"))
    print(exist(board, "ABCB"))
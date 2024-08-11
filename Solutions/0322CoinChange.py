import math
from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    dp = [math.inf] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            if i - c >= 0 and dp[i - c] < math.inf:
                dp[i] = min(dp[i], dp[i - c] + 1)
    return dp[-1] if dp[-1] < math.inf else -1

def coinChange2(coins: List[int], amount: int) -> int:
    memo = {}
    def dp(i):
        if i == 0:
            return 0
        if not i in memo:
            k = math.inf
            for c in coins:
                if i - c >= 0 and dp(i - c) >= 0:
                    k = min(k, dp(i - c))
            memo[i] = k + 1 if k < math.inf else -1
        return memo[i]
    return dp(amount)

if __name__ == '__main__':
    print(coinChange([1, 2, 5], 11))
    print(coinChange2([1, 2, 5], 11))
    print(coinChange([2], 3))
    print(coinChange2([2], 3))
    print(coinChange([1], 0))
    print(coinChange2([1], 0))
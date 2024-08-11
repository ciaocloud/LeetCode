from typing import List


def robMemo(nums: List[int]) -> int:
    memo = {}
    def decide(i):
        if i < 0:
            return 0
        if i == 0:
            return nums[0]
        if not i in memo:
            memo[i] = max(decide(i-1), decide(i - 2)+nums[i])
        return memo[i]
    return decide(len(nums)-1)

def rob(nums: List[int]) -> int:
    dp = [0] * (len(nums) + 1)
    dp[1] = nums[0]
    for i in range(1, len(nums)):
        dp[i+1] = max(dp[i], dp[i-1] + nums[i])
    return dp[len(nums)]

def robOpt(nums: List[int]) -> int:
    rob1 = rob2 = 0
    for i in range(len(nums)):
        rob1, rob2 = rob2, max(rob2, rob1 + nums[i])
    return rob2

if __name__ == '__main__':
    print(rob([1, 2, 3, 1]))
    print(rob([2,7,9,3,1]))
    print(rob([1, 1]))
    print(robOpt([1, 2, 3, 1]))
    print(robOpt([2,7,9,3,1]))
    print(robOpt([1, 1]))
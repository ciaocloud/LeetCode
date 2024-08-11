from typing import List


def rob(nums: List[int]) -> int:
    def robSub(arr: List[int]) -> int:
        rob1, rob2 = 0, 0
        for i in range(len(arr)):
            rob1, rob2 = rob2, max(rob1 + arr[i], rob2)
        return rob2
    return max(robSub(nums[:len(nums)-1]), robSub(nums[1:]))

if __name__ == '__main__':
    print(rob([2, 3, 2]))
    print(rob([1, 2, 3, 1]))
    print(rob([1, 2]))
    print(rob([1, 2, 3]))
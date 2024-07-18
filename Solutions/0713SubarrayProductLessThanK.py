from typing import List


def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    ans = i = j = 0
    product = 1
    while j < len(nums):
        product *= nums[j]
        j += 1
        while product >= k and i < j:
            product //= nums[i]
            i += 1
        ans += j - i
    return ans

if __name__ == '__main__':
    print(numSubarrayProductLessThanK([1, 2, 3], 0))
    print(numSubarrayProductLessThanK([10, 5, 2, 6], 100))
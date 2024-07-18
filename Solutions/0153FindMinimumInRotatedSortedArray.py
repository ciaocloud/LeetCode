from typing import List


def findMin(nums: List[int]) -> int:
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]

if __name__ == '__main__':
    print(findMin([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(findMin([3,4,5,1,2]))
    print(findMin([4,5,6,7,0,1,2]))
    print(findMin([3, 1, 2]))
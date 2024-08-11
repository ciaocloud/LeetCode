from typing import List


def findMin(nums: List[int]) -> int:
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        elif nums[mid] < nums[hi]:
            hi = mid
        else:
            hi -= 1
    return nums[lo]

def search(nums: List[int], target: int) -> int:
    def findMin(nums):
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return lo
    minIdx = findMin(nums)
    print("###", minIdx)
    def binsearch(nums, lo, hi):
        if lo > hi:
            return -1
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return binsearch(nums, mid+1, hi)
        else:
            return binsearch(nums, lo, mid-1)
    lo, hi = minIdx, len(nums) - 1
    if target > nums[-1]:
        lo, hi = 0, minIdx - 1
    return binsearch(nums, lo, hi)

if __name__ == '__main__':
    print(findMin([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(findMin([1,3,5]))
    print(findMin([2,2,2,0,1]))

    print(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
    print(search([4,5,6,7,0,1,2], 0))

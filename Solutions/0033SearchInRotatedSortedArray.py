from typing import List


def search(nums: List[int], target: int) -> int:
    def findMin():
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return lo

    minIndex = findMin()
    def binsearch(lo, hi):
        if lo > hi:
            return -1
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return binsearch(mid + 1, hi)
        return binsearch(lo, mid - 1)
    lo, hi = minIndex, len(nums) - 1
    if target > nums[-1]:
        lo, hi = 0, minIndex - 1
    return binsearch(lo, hi)

if __name__ == '__main__':
    print(search([1, 2, 3, 4, 5], 6))
    print(search([4,5,6,7,0,1,2], 0))
    print(search([4,5,6,7,0,1,2], 6))
    print(search([1], 0))

from typing import List


def findPeakElementRecursive(nums: List[int]) -> int:
    def binsearch(lo, hi):
        if lo == hi:
            return lo
        mid = lo + (hi - lo) // 2
        if nums[mid] > nums[mid + 1]:
            return binsearch(lo, mid)
        return binsearch(mid + 1, hi)
    return binsearch(0, len(nums) - 1)

def findPeakElementRecursive2(nums: List[int]) -> int:
    def binsearch(lo, hi):
        mid = lo + (hi - lo) // 2
        if nums[mid] > nums[mid + 1]:
            return binsearch(lo, mid)
        elif nums[mid] < nums[mid - 1]:
            return binsearch(mid + 1, hi)
        return mid

def findPeakElement(nums: List[int]) -> int:
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] > nums[mid + 1]:
            hi = mid
        else:
            lo = mid + 1
    return lo

def findPeakElementBruteForce(nums: List[int]) -> int:
    for i in range(len(nums)-1):
        if nums[i] > nums[i + 1]:
            return i
    return len(nums) - 1

if __name__ == '__main__':
    print(findPeakElementRecursive([1, 3, 5, 6, 7]))
    print(findPeakElement([1, 3, 5, 6, 7]))
    print(findPeakElementBruteForce([1, 3, 5, 6, 7]))
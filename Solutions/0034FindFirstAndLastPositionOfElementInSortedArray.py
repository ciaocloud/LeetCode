from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    def findLeftmost(nums, target):
        lo, hi = 0, len(nums) - 1
        leftmost = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                leftmost = mid
                lo = mid + 1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return leftmost


        # while lo < hi:
        #     mid = lo + (hi - lo) // 2
        #     if nums[mid] < target:
        #         lo = mid + 1
        #     else:
        #         hi = mid
        # return lo if nums[lo] == target else -1

    fist = findLeftmost(nums, target)

    def findRightmost(nums, target):
        lo, hi = 0, len(nums) - 1
        rightmost = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                rightmost = mid
                hi = mid - 1
            if nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return rightmost
        # return hi - 1 if hi > 0 and nums[hi - 1] == target else -1

    last = findRightmost(nums, target)

    return [first, last]


if __name__ == '__main__':
    print(searchRange([1, 2, 3, 4], 4))
    print(searchRange([2, 2], 3))
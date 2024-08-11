import math
from typing import List

def minEatingSpeed(piles: List[int], h: int) -> int:
    def canFinish(v):
        k = 0
        for p in piles:
            k += math.ceil(p / v)
            if k > h:
                return False
        return True

    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if canFinish(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

def minEatingSpeedSortFirst(piles: List[int], h: int) -> int:
    piles.sort()
    def findFirstLarger(target):
        lo, hi = 0, len(piles)-1
        while lo < hi:
            mid = lo + (hi-lo)//2
            if piles[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def canFinish(v):
        k = findFirstLarger(v)
        for j in range(k, len(piles)):
            k += piles[j] // v
            if piles[j] % v != 0:
                k += 1
            if k > h:
                return False
        return True

    # def canFinish(v):
    #     k = 0
    #     for i in range(len(piles)):
    #         if piles[i] < v:
    #             k += 1
    #         else:
    #             k += piles[i] // v
    #             if piles[i] % v != 0:
    #                 k += 1
    #         if k > h:
    #             return False
    #     return True


    lo, hi = 1, piles[-1]
    while lo < hi:
        mid = lo + (hi-lo)//2
        if canFinish(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

if __name__ == '__main__':
    print(minEatingSpeed([3,6,7,11], 8))
    print(minEatingSpeedSortFirst([3,6,7,11], 8))
    print(minEatingSpeed([30,11,23,4,20], 6))
    print(minEatingSpeedSortFirst([30,11,23,4,20], 5))
    print(minEatingSpeed([30,11,23,4,20], 6))
    print(minEatingSpeedSortFirst([30,11,23,4,20], 5))
    print(minEatingSpeed([312884470], 312884469))
    print(minEatingSpeedSortFirst([312884470], 312884469))


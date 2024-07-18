from typing import List


def findKClosestElementsSort(arr: List[int], k: int, x: int) -> List[int]:
    sorted_arr = sorted(arr, key=lambda y: abs(y-x))
    topK = sorted_arr[:k]
    return sorted(topK)

def findKClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    def dist(i):
        return abs(x-arr[i])
    lo, hi = 0, len(arr)-1
    while lo < hi:
        mid = lo + (hi-lo)//2
        if dist(mid) < dist(mid+1):
            hi = mid
        else:
            lo = mid + 1
    hi = lo
    while hi - lo + 1 < k:
        if lo > 0 and hi < len(arr)-1:
            if dist(lo-1) <= dist(hi+1):
                lo -= 1
            else:
                hi += 1
        if lo > 0:
            lo -= 1
        elif hi < len(arr)-1:
            hi += 1
        else:
            break
    print(lo, hi)
    return arr[lo:hi+1]

if __name__ == '__main__':
    print(findKClosestElements([1,2,3,4,5], 4, 3))


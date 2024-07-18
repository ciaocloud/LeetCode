import random
from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    # ## Min Heap
    # heap = []
    # for num in nums:
    #     heapq.heappush(heap, num)
    #     if len(heap) > k:
    #         heapq.heappop(heap)
    # return heap[0]

    # ## Max Heap
    # maxHeap = [-num for num in nums]
    # heapq.heapify(maxHeap)
    # ans = -1
    # for _ in range(k):
    #     ans = -heapq.heappop(maxHeap)
    # return ans

    ## Quick
    quickSelect(nums, 0, len(nums) - 1, k)
    # print(nums)
    return nums[k - 1]
def quickSelect(nums, lo, hi, k):
    if lo >= hi:
        return
    p = partition(nums, lo, hi)
    if p == k:
        return
    elif p < k:
        quickSelect(nums, p + 1, hi, k)
    else:
        quickSelect(nums, lo, p - 1, k)

def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]

def partition(nums, l, r):
    p = random.randint(l, r)
    swap(nums, p, r)  ## put the pivot at r
    i = l
    for j in range(l, r):
        if nums[j] >= nums[r]:
            swap(nums, i, j)
            i += 1
    swap(nums, i, r)  ## put the pivot at i
    return i



if __name__ == '__main__':
    nums = [3,3,3,3,4,3,3,3,3]
    k = 5
    print(findKthLargest(nums, k))

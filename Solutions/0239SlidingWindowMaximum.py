import collections
from typing import List


## Monotone Queue
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    mq = collections.deque()
    ans = []
    for i, v in enumerate(nums):
        while mq and i - mq[0] >= k:
            mq.popleft()  ## remove those too old (must leave)
        while mq and v >= nums[mq[-1]]:
            mq.pop()  ## remove those no better than the newest (can never have a chance any more)
        mq.append(i)  ## newest must be added (anything is possible in the future)
        if i >= k - 1:
            ans.append(nums[mq[0]])
    return ans

if __name__ == '__main__':
    print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
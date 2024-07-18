import heapq
from typing import List


def furthestBuilding(heights: List[int], bricks: int, ladders: int) -> int:
    ladderHeap = []
    for i in range(1, len(heights)):
        diff = heights[i] - heights[i-1]
        if diff <= 0:
            continue
        if len(ladderHeap) < ladders:
            heapq.heappush(ladderHeap, (diff, i))
            continue
        if ladderHeap and ladderHeap[0][0] < diff:
            minLadder, j = heapq.heappop(ladderHeap)
            bricks -= minLadder
            if bricks < 0:
                return i-1
            heapq.heappush(ladderHeap, (diff, i))
        else:
            bricks -= diff
            if bricks < 0:
                return i-1

    return len(heights)-1

if __name__ == '__main__':
    heights = [4,2,7,6,9,14,12]
    bricks = 5
    ladders = 1
    print(furthestBuilding(heights, bricks, ladders))

    heights = [14, 3, 19, 3]
    bricks = 17
    ladders = 0
    print(furthestBuilding(heights, bricks, ladders))
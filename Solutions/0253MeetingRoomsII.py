import heapq
from typing import List


def minMeetingRooms(intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: x[0]) ## sort by starting time
    pq = []
    for start, end in intervals:
        if pq and pq[0] <= start:
            heapq.heappop(pq)
        heapq.heappush(pq, end)
    return len(pq)

if __name__ == '__main__':
    print(minMeetingRooms([[1, 2], [3, 4], [5, 6]]))
    print(minMeetingRooms([[2,11],[6,16],[11,16]]))
    print(minMeetingRooms([[9,16],[6,16],[1,9],[3,15]]))
    print(minMeetingRooms([[2,15],[36,45],[9,29],[16,23],[4,9]]))
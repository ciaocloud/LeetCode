from typing import List
import heapq

def mostBooked(n: int, meetings: List[List[int]]) -> int:
    unused, used = list(range(n)), []
    cnts = [0] * n
    meetings.sort()
    for start, end in meetings:
        while used and used[0][0] <= start:
            _, j = heapq.heappop(used)
            heapq.heappush(unused, j)
        if unused:
            j = heapq.heappop(unused)
            heapq.heappush(used, (end, j))
            cnts[j] += 1
        else:
            earliestEnd, j = heapq.heappop(used)
            earliestEnd += end - start
            heapq.heappush(used, (earliestEnd, j))
            cnts[j] += 1
    return cnts.index(max(cnts))

if __name__ == '__main__':
    print(mostBooked(2, [[0,10],[1,5],[2,7],[3,4]]))
    print(mostBooked(4, [[18,19],[3,12],[17,19],[2,13],[7,10]]))
    print(mostBooked(4, [[48,49],[22,30],[13,31],[31,46],[37,46],[32,36],[25,36],[49,50],[24,34],[6,41]])) ## 0
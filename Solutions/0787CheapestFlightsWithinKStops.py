import collections
import heapq
import math
from typing import List


def findCheapestPriceBellmanFord(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    costs = [math.inf] * n
    costs[src] = 0
    for i in range(k+1):
        # newCosts = [math.inf] * n
        newCosts = costs[:]
        for u, v, w in flights:
            # newCosts[v] = min(costs[v], costs[u] + w)
            if costs[u] < math.inf and costs[u] + w < costs[v]:
                newCosts[v] = costs[u] + w
        costs = newCosts
    return costs[dst] if costs[dst] < math.inf else -1

def findCheapestPriceBfs(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    graph = collections.defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))
    costs = [math.inf] * n
    queue = collections.deque([(src, 0)])
    step = 0
    while queue and step <= k:
        for _ in range(len(queue)):
            u, cost = queue.popleft()
            for v, w in graph[u]:
                if cost + w < costs[v]:
                    costs[v] = cost + w
                    queue.append((v, cost + w))
        step += 1
    return costs[dst] if costs[dst] < math.inf else -1

def findCheapestPriceDijkstra(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    graph = collections.defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))
    # costs = [math.inf] * n
    # costs[src] = 0

    stops = [k+1] * n
    # stops[src] = 0

    pq = [(0, src, 0)]
    while pq:
        cost, u, steps = heapq.heappop(pq)
        if steps > k + 1 or steps > stops[u]:
            continue
        stops[u] = steps
        if u == dst:
            return cost
        for v, w in graph[u]:
            heapq.heappush(pq, (cost + w, v, steps + 1))
            # if cost + w < costs[v]:
            #     costs[v] = cost + w
            #     heapq.heappush(pq, (costs[v], v, steps + 1))
    return -1

if __name__ == '__main__':
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    n, src, dst, k = 4, 0, 3, 1
    print(findCheapestPriceDijkstra(n, flights, src, dst, k))
    print(findCheapestPriceBellmanFord(n, flights, src, dst, k))

    flights = [[0,1,20],[1,2,20],[2,3,30],[3,4,30],[4,5,30],[5,6,30],[6,7,30],[7,8,30],[8,9,30],[0,2,9999],[2,4,9998],[4,7,9997]]
    ## 0 -> 2 -> 4 -> 7 -> 8 -> 9  (9997 + 30 + 30)
    n, src, dst, k = 10, 0, 9, 4
    print(findCheapestPriceDijkstra(n, flights, src, dst, k))
    print(findCheapestPriceBellmanFord(n, flights, src, dst, k))

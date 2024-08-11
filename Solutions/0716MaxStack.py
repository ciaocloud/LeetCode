import heapq
from sortedcontainers import SortedList


class MaxStackWithSortedList:
    def __init__(self):
        self.stack = SortedList()
        self.values = SortedList()
        self.i = 0

    def push(self, x: int) -> None:
        self.stack.add((self.i, x))
        self.values.add((x, self.i))
        self.i += 1

    def pop(self) -> int:
        i, v = self.stack.pop()
        self.values.remove((v, i))
        return v

    def top(self) -> int:
        return self.stack[-1][1]

    def peekMax(self) -> int:
        return self.values[-1][0]

    def popMax(self) -> int:
        v, i = self.values.pop()
        self.stack.remove((i, v))
        return v
class MaxStack:
    def __init__(self):
        self.heap = []
        self.stack = []
        self.i = 0
        self.toRemove = set()

    def push(self, x: int) -> None:
        heapq.heappush(self.heap, (-x, -self.i))
        self.stack.append((x, self.i))
        self.i += 1

    def pop(self) -> int:
        while self.stack and self.stack[-1][1] in self.toRemove:
            self.stack.pop()
        v, i = self.stack.pop()
        self.toRemove.add(i)
        return v

    def top(self) -> int:
        while self.stack and self.stack[-1][1] in self.toRemove:
            self.stack.pop()
        return self.stack[-1][0]

    def peekMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.toRemove:
            heapq.heappop(self.heap)
        return -self.heap[0][0]

    def popMax(self) -> int:
        while self.heap and self.heap[0][1] in self.toRemove:
            heapq.heappop(self.heap)
        v, i = heapq.heappop(self.heap)
        self.toRemove.add(-i)
        return -v
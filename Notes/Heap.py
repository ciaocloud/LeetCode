


class Heap:
    def __init__(self, arr=[]):
        self.heap = self.buildHeap([None].extend(arr))
        self.heapSize = len(self.heap)
    def parent(self, index):
        return index//2

    def left(self, index):
        return 2*index

    def right(self, index):
        return 2*index+1

    def sink(self, i, arr=None, heapSize=None):
        if arr is None:
            arr = self.heap
        if heapSize == None:
            heapSize = self.heapSize
        l, r = self.left(i), self.right(i)
        ## heapify a max heap
        maxIndex = i
        if l < heapSize and arr[l] > arr[maxIndex]:
            maxIndex = l
        if r < heapSize and arr[r] > arr[maxIndex]:
            maxIndex = r
        if maxIndex != i:
            print("max index=", maxIndex)
            arr[i], arr[maxIndex] = arr[maxIndex], arr[i]
            self.sink(maxIndex, arr, heapSize)

    def buildHeap(self, arr):
        heapSize = len(arr)
        # print(len(arr))
        ## Time complexity: O(N), instead of O(NlogN)
        for i in reversed(range(len(arr)//2+1)):
            self.sink(i, arr, heapSize)
            print("##", i)
            print("###", arr)
        return arr

    def heapsort(self, arr=None):
        arr = self.buildHeap(arr)
        for i in reversed(range(len(arr))):
            arr[0], arr[i] = arr[i], arr[0]
            heapSize = i + 1
            self.sink(0, arr, heapSize)

    def peekMax(self):
        return self.heap[0]

    def popMax(self):
        maxVal = self.heap[0]
        self.heap[0] = self.heap[self.heapSize-1]
        self.heapSize -= 1
        self.sink(0, self.heap, self.heapSize)
        return maxVal

    def swim(self, i):
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def insert(self, val):
        self.heap.append(val)
        self.heapSize += 1
        self.swim(len(self.heap)-1)

if __name__ == '__main__':
    arr = [3, 1, 2]
    # maxHeap = Heap(arr)
    # maxHeap.sink(0, arr)
    # print(maxHeap.heap)

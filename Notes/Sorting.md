# Counting Sort
- Iterate through the input, counting the # of times each item occurs, and using the counts to compute an item's index in the final sorted array.

1. count the frequencies
2. compute frequency cumulates (which specify destinations)
3. access cumulates using key as index to **move items** (easier from tail to head)
4. copy back into original array if needed
```Python
for i in range(len(A)):
    j = A[i]
    count[j] += 1
for i in range(R):
    count[i] += count[i-1]
for i in reversed(range(len(A))): ## for (int i = len(A); i >= 0; i--)
    j = A[i]
    count[j] -= 1 ## position of the last j (i.e., there are count[j] values <= j)
    aux[count[j]] = j 
```


### Dutch National Flag Problem
The Dutch national flag problem can be solved using counting sort. We don't even need to accumulate the counts and compute the positions. Instead we can simply place `count[i]` copies of `nums[i]` to the output (we don't even need an extra auxiliary array).

But the Dutch national flag problem can be better solved using 3-pointers. The left pointer indicates the rightmost boundary of 0s, while the right pointer indicates the leftmost boundary of 2s, and the current pointer is the index of the current element we are working on.
```Python
lo, i, hi = 0, 0, len(nums)-1
while i <= hi:
    if nums[i] == 0:
        nums[lo], nums[i] = nums[i], nums[lo]
        i += 1
        lo += 1
    elif nums[i] == 1:
        i += 1
    else:
        nums[i], nums[hi] = nums[hi], nums[i]
        hi -= 1
```

## LC 274. H-index
- Sort citation numbers first ($\mathcal{O}(\log(N))$), the number of papers that were cited $\ge h$ times is the largest $h=n-i$, or smallest $i$.
```Python
n = len(citations)
citations.sort()
for i in range(n):
    if n - i <= citations[i]:
        return n-i
return 0
```

### Binary search to search in the sorted array (LC 275. H-index II)
- Given a sorted listed, find the first i s.t. $n-i \le$ citations[i]
```Python


```

- Couting sort
```Python
n = len(citations)
counts = [0] * (n + 1)
for c in citations:
    if c > n:
        counts[n] += 1
    else:
        counts[c] += 1
k = 0
for h in reversed(range(n+1)):
    k += counts[h]
    if k >= h:
        return h
return 0
```

### LC 912. Sort an array
- Use Counting sort
```Python
def sortArray(self, nums: List[int]) -> List[int]:
    counts = collections.defaultdict(int)
    for v in nums:
        counts[v] += 1

    # keys = sorted(list(counts.keys()))
    # i = 0
    # for num in keys:
    #     for j in range(counts[num]):
    #         nums[i] = num
    #         i += 1

    i = 0
    for v in range(min(nums), max(nums)+1):
        while counts[v] > 0:
            nums[i] = v
            i += 1
            counts[v] -= 1
    return nums

```

## Selection Sort
```python
def selectionSort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

```
## Insertion Sort

- TODO: Merge sort, Quick sort, Radix sort
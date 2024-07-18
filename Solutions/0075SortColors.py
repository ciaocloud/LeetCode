from typing import List


def sortColors(nums: List[int]) -> List[int]:
    def swap(i, j):
        nums[i], nums[j] = nums[j], nums[i]

    i, j, k = 0, 0, len(nums) - 1
    while j <= k:
        if nums[j] == 0:
            swap(i, j)
            i += 1
            j += 1
        elif nums[j] == 1:
            j += 1
        else:
            swap(j, k)
            k -= 1
    return nums

if __name__ == '__main__':
    print(sortColors([1, 0, 0]))
    print(sortColors([2, 1, 0]))
    print(sortColors([2,0,2,1,1,0]))

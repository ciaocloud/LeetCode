from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    m = dict()
    for i, num in enumerate(nums):
        if target - num in m:
            return [m.get(target - num), i]
        else:
            m[num] = i
    raise Exception("Result not found")

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))
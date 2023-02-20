
#Two pointers
from typing import List

def removeElement(nums: List[int], val : int) -> int:
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    print(nums)
    return i


nums = [1, 4, 5, 0, 2, 2, 3, 2]

a = removeElement(nums, 2)
print(a)
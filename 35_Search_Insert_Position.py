from typing import List

# Binary search
#1 Iterative Method
def searchInsert(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high)//2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return low


nums = [1, 3, 5, 6]
target = 2

print(searchInsert(nums, target))

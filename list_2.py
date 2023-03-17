# Write a python function that takes as parameters a list of integers and a target value,
# it sorts the list in ascending order and returns the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

def binarySearch(nums, target): 
    if len(nums) == 0: 
        return 0

    # Sort the list
    nums.sort()

    # Binary search
    left = 0
    right = len(nums) - 1
    while left <= right: 
        mid = (left + right) // 2

        if nums[mid] == target: 
            return mid 
        elif nums[mid] < target: 
            left = mid + 1
        else: 
            right = mid - 1

    # Target not found, return index where it would be inserted
    return left

# Test Case One 
nums = [1,3,5,6]
target = 5

index = binarySearch(nums, target)
print("Index of target in sorted list:", index)
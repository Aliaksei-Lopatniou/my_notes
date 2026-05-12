#linear search

def linear_search(nums, target): #O(n==len(nums))
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


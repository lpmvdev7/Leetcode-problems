# Leetcode numero 33 Search in Rotated Sorted Array

def search(nums, target):
    index = 0
    for i, n in enumerate(nums):
        if n == target:
            return i
        else:
            index = -1
    return index

nums = [4,5,6,7,0,1,2]
target = 7

call = search(nums, target)
print(call)

# Leetcode numero 136. Single Number

def singleNumber(nums):
    for n in nums:
        aparicion = nums.count(n)
        if aparicion == 1:
            return n 


nums = [2,2,5,5,5,6,5,6,9]
call = singleNumber(nums)

print(call)

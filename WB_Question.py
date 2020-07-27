# Remove Element
# Given a list of numbers and a value as input to a function, remove all instances of that value "in-place" and return the new length of the list
# Input: nums = [3,2,2,3] value = 3
# Output: return a length == 2

# def remove_element(nums,target):
#     while target in nums:
#         nums.remove(target)
#     return len(nums)

# target = 3
# nums = [3,2,2,35,3,7,-3]
# print(remove_element(nums, target))

def remove_element(nums,target):
    for num in nums:
        if target == num:
            nums.remove(target)
    return len(nums)

target = 3
nums = [3,2,2,35,3,7,-3]
print(remove_element(nums, target))
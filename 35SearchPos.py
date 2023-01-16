def SearchPos(nums, target):
    
    if target not in nums:
        nums.append(target)
    nums.sort()
    return nums.index(target)






nums = [1,3,5,6]
target = 6
a = SearchPos(nums,target)
print(a)
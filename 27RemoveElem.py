def DelE(nums, val):
    i = 0
    while i <len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i +=1
    return nums
nums = [0,1,2,2,3,0,4,2]
d =DelE(nums,2)
k = len(nums)
print(k, d)

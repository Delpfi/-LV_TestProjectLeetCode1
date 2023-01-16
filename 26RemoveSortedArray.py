def RemoteArray(nums):
    i=1
    while i < len(nums):
        a1 = nums[i]
        a2 = nums[i-1]
        if a1 == a2:
            nums.pop(i)
        else:
            i +=1


nums = [1,1,2]
RemoteArray(nums)
k = len(nums)
print(k, nums)



def find(nums, tar):
    y = -1
    ArrT = [-1,-1]
    if not target in nums:
        return ArrT
    ArrT[0] = nums.index(tar)
    """
    for i in nums:
        y +=1
        if i == tar:
            ArrT[1] =y
    return ArrT
    """
    l = len(nums) -1
    while l >= 0:
        n = nums[l]
        if n == target:
            ArrT[1] = l
            return ArrT
        l-=1


nums = [5,7,7,8,8,10]
target = 8
a = find(nums, target)
print(a)
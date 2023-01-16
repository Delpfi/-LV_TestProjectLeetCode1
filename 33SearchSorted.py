def searchNom(nums, target):
    i =0
    l = len(nums)
    ArrN = [-1, ]
    if not target in nums:
        return ArrN
    ArrN[0] = nums.index(target)
    return ArrN

    """
    ArrN=[-1,]
    while i < l:
        ch = nums[i]

        if ch == target:
            ArrN[0] = i
            return ArrN
        i+=1
    return ArrN
    """


nums = [4,5,6,7,0,1,2]
target = 3

a = searchNom(nums, target)
print(a)
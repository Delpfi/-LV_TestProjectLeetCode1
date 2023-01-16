nums = [-1,2,1,-4]
nums1 = sorted(nums)
target = 1
d = len(nums)
result = float('inf')

for i in range(d):
    j = i+1
    k = d-1
    while j<k:
        s = nums1[i] + nums1[j] + nums1[k]
        #if s == target:
        #   print(s)
        k1 = target - s
        k2 = target-result
        if abs(k1) < abs(k2):
            result = s

        if s>target:
            k -=1
        else:
            j +=1

print(result)
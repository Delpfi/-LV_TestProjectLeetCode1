nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

for i in nums2:
    nums1[m] = i
    m+=1
nums1.sort()
print(nums1)
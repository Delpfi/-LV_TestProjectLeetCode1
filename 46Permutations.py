import copy


class Solution:
    def permute(self, numss):


        Res = []
        head =[]
        self.perest(head,numss,Res,)
        return Res

    def perest(self, head,Fortail, Res):

        if not Fortail and head not in Res:
            Res.append(head)
            return Res

        for i in Fortail:
            Fort = copy.deepcopy(Fortail)
            head1 = head[:]
            head1.append(i)
            ind = Fortail.index(i)
            Fort.pop(ind)
            self.perest(head1,Fort,Res)
nums = [1,2,1]
nums1 =nums
a = Solution()
Res1 = a.permute(nums1)

print(Res1)
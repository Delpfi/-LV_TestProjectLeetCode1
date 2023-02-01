class Solution:
    def groupAnagrams(self, strs):
        strs1 = {}
        Res = []
        n = len(strs)
        strs3 = sorted(strs)
        st1 = lambda str1, str2: sorted(str1) == sorted(str2)
        """
        for s in strs:
            str1 = str(sorted(s))
            if str1 in strs1:
                strs1[str1].append(s)
            else:
                strs1[str1] = [s]
        return strs1.values()
        """








strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

a = Solution()
Res = a.groupAnagrams(strs)
print(list(Res))


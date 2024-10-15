class Solution(object):
    def isIsomorphic(self, s, t):
        map1 = []
        map2 = []
        for idx in s:
            map1.append(s.index(idx))
        for idx in t:
            map2.append(t.index(idx))
        if map1 == map2:
            return True, map1, map2
        return False

a = Solution()
print(a.isIsomorphic(s="egg", t="add"))

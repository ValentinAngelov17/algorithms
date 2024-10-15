class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        un = []
        s1, s2 = s1.split(), s2.split()
        for word in s1:
            q = s1.count(word)
            if q < 2 and word not in s2:
                un.append(word)
        for word in s2:
            q = s1.count(word)
            if q < 2 and word not in s1:
                un.append(word)
        return un


a = Solution()
print(a.uncommonFromSentences(s1="abcd def abcd xyz", s2="ijk def ijk"))

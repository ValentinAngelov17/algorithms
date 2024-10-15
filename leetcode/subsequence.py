class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        value = 0
        for i in range(len(t)):
            char = s[value]
            if char == t[i]:
                value += 1
            if value == len(s):
                break

        if value == len(s):
            return True
        else:
            return False


a = Solution()
print(a.isSubsequence("b", "abc"))

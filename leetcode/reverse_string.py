class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        return " ".join(s[::-1])


a = Solution()
print(a.reverseWords("  a good   example"))

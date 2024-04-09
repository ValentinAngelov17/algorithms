from roman import fromRoman
class Solution:
    def romanToInt(self, s: str):
        r = fromRoman(s)
        print(r)

Solution().romanToInt("IV")
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opening_brackets = []
        closing_brackets = []
        dicty = {"(": ")", "{": "}", "[": "]"}
        for char in range(len(s)):
            if s[char] in "([{":
                opening_brackets.append(s[char])
            else:
                if len(opening_brackets) == 0:
                    return False
                closing_brackets.append(s[char])
                current = opening_brackets.pop()

                if s[char] == dicty[current]:
                    closing_brackets.pop()
                    continue
                else:
                    return False
        if opening_brackets or closing_brackets:
            return False
        else:
            return True



a = Solution()
print(a.isValid("]"))

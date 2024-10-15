class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()

        r = ""
        for char in s:
            if char.isalpha() or char.isdigit():
                r += char
        l = len(r)

        if l % 2 == 0:
            half_l = int(l / 2)
            right = r[half_l:]
            right_reverse = right[::-1]
            left = r[:half_l]

        else:
            half_l = l // 2
            right = r[half_l + 1:]
            right_reverse = right[::-1]
            left = r[:half_l]
        if left == right_reverse:
            return True
        else:
            return False


a = Solution()
print(a.isPalindrome(s="0P"))

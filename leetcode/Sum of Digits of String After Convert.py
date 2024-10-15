class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        char_sum = ""
        char_nums = 0
        for char in s:
            summary = ord(char) - 96
            char_sum += str(summary)

        for transform in range(k):
            for num in char_sum:
                char_nums += int(num)
            char_sum = str(char_nums)
            char_nums = 0

        return int(char_sum)


a = Solution()
print(a.getLucky(s = "leetcode", k = 2))

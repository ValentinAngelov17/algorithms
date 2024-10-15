class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        start_index = 0
        end_index = 0

        string_output_length = 0
        if t in s:
            return 0
        


a = Solution()
print(a.minWindow(s="ABECODEBANC", t="ABC"))

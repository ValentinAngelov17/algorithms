class Solution(object):
    def isAnagram(self, s, t):
        s_dict = {}
        t_dict = {}
        if len(s) != len(t):
            return "false"
        for i in range(len(s)):
            char1 = s[i]
            char2 = t[i]
            if char1 in s_dict:
                s_dict[char1] += 1
            else:
                s_dict[char1] = 1

            if char2 in t_dict:
                t_dict[char2] += 1
            else:
                t_dict[char2] = 1

        if sorted(s_dict) == sorted(t_dict):
            for key, value in s_dict.items():
                for key1,value1 in t_dict.items():
                    pass
        else:
            return "false"


a = Solution()
print(a.isAnagram("aacc", "ccac"))

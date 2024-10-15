from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1

            result[tuple(count)].append(s)

        return result.values()


a = Solution()
print(a.groupAnagrams(strs=["act", "pots", "tops", "cat", "stop", "hat"]))

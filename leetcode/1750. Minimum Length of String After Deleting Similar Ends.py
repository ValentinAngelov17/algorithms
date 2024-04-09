class Solution:
    def minimumLength(self, s: str) -> int:
        length = len(s)
        counter = 0
        while counter < length // 2:
            if len(s) <= 2:
                break

            start_index = 0
            end_index = len(s) - 1
            if s[start_index] == s[end_index]:
                counter += 1

        return len(s) - counter * 2


Solution().minimumLength("aabaa")

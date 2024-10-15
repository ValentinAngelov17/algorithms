class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        max_value = 0

        for number in range(len(citations)):
            h_index = citations[number]
            counter = 0
            for num in citations:
                value = num - h_index
                if value >= 0:
                    counter += 1

            if counter >= h_index >= max_value:
                max_value = h_index

        if len(citations) == 1:
            return 1
        elif len(citations) == 0:
            return 0
        else:
            return max_value


a = Solution()
print(a.hIndex([100]))

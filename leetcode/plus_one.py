class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = ""
        for digit in digits:
            result += str(digit)
        result = int(result) + 1
        chars = str(result)
        return [int(char) for char in chars]


a = Solution()
print(a.plusOne(digits=[9]))

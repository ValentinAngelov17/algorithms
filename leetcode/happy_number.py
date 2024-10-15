class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result = str(n)

        numbers = []
        while True:
            current_sum = 0
            for number in result:
                current_sum += int(number) ** 2
            result = current_sum

            if result in numbers:
                return False
            elif result == 1:
                return True
            numbers.append(result)
            result = str(result)


a = Solution()
print(a.isHappy(2))

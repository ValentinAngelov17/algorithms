class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        observation_sum = sum(rolls)
        right = (mean + n) * mean - observation_sum

        base = right // n
        remainder = right % n
        result = [base] * n
        for r in range(remainder):
            result[r] += 1

        return result


a = Solution()
print(a.missingRolls([1,2,3,4], mean=6, n=4))

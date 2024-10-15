class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        allSum = 0

        # Calculate the total sum of all elements in the chalk array
        for val in chalk:
            allSum += val

        # Calculate the remainder of k when divided by allSum
        # This determines how much chalk remains after several full cycles
        mod = k % allSum

        # Get the number of students
        n = len(chalk)

        # Iterate through the chalk array
        for i in range(n):
            # If the current student's chalk usage is more than the remaining chalk, return their index
            if chalk[i] > mod:
                return i

            # Otherwise, subtract the current student's chalk usage from the remaining chalk
            mod -= chalk[i]

        # This line should never be reached since the problem guarantees a solution.
        return mod


a = Solution()
print(a.chalkReplacer(
    [93, 87, 71, 59, 95, 27, 74, 37, 24, 40, 95, 36, 12, 96, 19, 36, 78, 43, 25, 22, 18, 93, 69, 72, 34, 44, 11, 60, 62,
     26, 97, 67, 45, 100, 48, 14, 51, 81, 17, 6, 88, 63, 79, 80, 36, 14, 49, 21, 41, 23, 10, 7, 83, 50, 50, 95, 91, 100,
     14, 73, 40, 55, 46, 84, 81, 56, 73, 89, 97, 18, 22, 48, 78, 54, 27, 91, 19, 65, 88, 28, 80, 21, 12, 55, 23, 3, 36,
     38, 64, 45, 84, 83, 54, 77, 45, 30, 73, 59, 31, 90, 20, 39, 57, 27, 35, 55, 93, 12, 46, 43, 17, 95, 25, 90, 97, 74,
     58, 1, 92, 38, 15, 85, 59, 52, 79], k=984068366
    ))

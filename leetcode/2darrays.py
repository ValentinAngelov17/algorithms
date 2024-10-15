class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        new_list = []
        if len(original) == m * n:
            pass
        else:
            return []
        first_index = 0
        j = n
        for _ in range(m):
            current_list = original[first_index:j]
            new_list.append(current_list)

            if n == 1:
                j += 1
                first_index += 1
            else:
                j += n
                first_index += n
            if n >= len(original) + 1:
                break

        return new_list


a = Solution()
print(a.construct2DArray(original=[3, 2, 3, 1, 5, 2], m=3, n=2))

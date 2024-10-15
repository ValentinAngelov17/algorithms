class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        ratings_len = len(ratings)
        children_candy = [1 for _ in range(ratings_len)]

        for i in range(ratings_len):
            if i == 0 and ratings_len > 0:
                if ratings[i] > ratings[i + 1]:
                    children_candy[i] = children_candy[i + 1] + 1

            elif i == ratings_len - 1:
                if ratings[i] > ratings[i - 1]:
                    children_candy[i] = children_candy[i - 1] + 1
            else:
                if ratings[i] > ratings[i - 1]:
                    children_candy[i] = children_candy[i - 1] + 1
                if ratings[i] > ratings[i + 1]:
                    children_candy[i] = children_candy[i + 1] + 1

        return sum(children_candy)


a = Solution()
print(a.candy([1,2,87,87,87,2,1]))

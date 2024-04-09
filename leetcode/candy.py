class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        result = [1] * n
        for i in range(len(ratings)):
            if i == 0 or i == len(ratings):
                if ratings[i] > ratings[i+1]:
                    pass
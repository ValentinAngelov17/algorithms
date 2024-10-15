class Solution:
    def dailyTemperatures(self, temperatures):
        result = []
        for day in range(len(temperatures)):
            temp = temperatures[day]
            counter = 0
            for second in range(day, len(temperatures)):
                if temperatures[second] < temp:
                    counter += 1

            result.append(counter)
        return result


a = Solution()
print(a.dailyTemperatures(temperatures=[30, 38, 30, 36, 35, 40, 28]))

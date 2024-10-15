class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(numbers)):
            indexes = [i + 1]

            current_sum = numbers[i]
            for j in range(i + 1, len(numbers)):
                next = numbers[j]

                if current_sum > target:
                    break
                elif current_sum < target:
                    current_sum += next
                    indexes.append(j + 1)
                else:
                    return indexes


a = Solution()
print(a.twoSum(numbers=[2, 3, 4], target=6))

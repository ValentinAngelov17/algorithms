class Solution:
    def topKFrequent(self, nums: list[int], k: int):
        output = {}
        for num in nums:
            if num in output:
                output[num] += 1
            else:
                output[num] = 1

        freq_values = sorted(output.values(), reverse=True)
        if k <= len(freq_values):
            b = freq_values[k - 1]
        else:
            return []

        result_keys = [key for key, value in output.items() if value == b]

        return result_keys


a = Solution()
print(a.topKFrequent(nums=[7, 7], k=1))

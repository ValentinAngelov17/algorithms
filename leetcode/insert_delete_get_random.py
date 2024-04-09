class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        total_product = 1
        zero_count = 0

        for num in nums:
            if num != 0:
                total_product *= num
            else:
                zero_count += 1

        result = []

        if zero_count > 1:
            return [0] * len(nums)

        for num in nums:
            if num != 0:
                if zero_count == 1:
                    result.append(0)
                else:
                    result.append(total_product // num)
            else:
                result.append(total_product)

        return result


print(Solution().productExceptSelf([1, 2, 3, 4]))

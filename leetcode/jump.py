def can_jump(nums: list[int]) -> bool:
    current_index = 0
    while True:
        is_true = False
        start_index = nums[current_index]
        if start_index == len(nums) - 1 or len(nums) == 1:
            is_true = True
            break
        elif start_index >= len(nums) or nums[current_index] == 0:
            break
        current_index += start_index
    return is_true

print(can_jump([2, 0]))


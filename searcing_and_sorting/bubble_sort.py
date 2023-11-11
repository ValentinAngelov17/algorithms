numbers = [int(x) for x in input().split()]
counter = 0
is_sorted = False
while not is_sorted:
    is_sorted = True
    for idx in range(1, len(numbers) - counter):
        if numbers[idx] < numbers[idx - 1]:
            numbers[idx], numbers[idx - 1] = numbers[idx - 1], numbers[idx]
            is_sorted = False
    counter += 1

print(*numbers, sep=' ')

prices = [7,1,5,3,6,4]
def best_time_to_buy(prices: list):
    value = 0
    for i in range(len(prices) - 1):
        lowest_number = prices[i]
        max_number = max(prices[i+1:])
        if (max_number - lowest_number) >= value:
            value = max_number - lowest_number
    return value


print(best_time_to_buy(prices))


# Apple Stocks
# O(n) time
# O(1) space

def get_max_profit(stock_prices):
    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for i in range(1, len(stock_prices)):
        profit = stock_prices[i] - min_price
        max_profit = max(profit, max_profit)
        min_price = min(stock_prices[i], min_price)

    return max_profit

def get_best_buy_sell_times(stock_prices):
    buy_idx = 0
    sell_idx = 1
    previous_profit = stock_prices[sell_idx] - stock_prices[buy_idx]

    for i in range(1, len(stock_prices)):
        current_profit = stock_prices[i] - stock_prices[buy_idx]

        if current_profit > previous_profit:
            sell_idx = i
        if stock_prices[i] < stock_prices[buy_idx]:
            buy_idx = i

        previous_profit = current_profit

    return [buy_idx, sell_idx]

print get_max_profit([10, 7, 5, 8, 11, 9])
print get_max_profit([10, 7, 5, 2, 1, 0])
print get_best_buy_sell_times([10, 7, 5, 8, 11, 9])
print get_best_buy_sell_times([10, 7, 5, 2, 1, 0])

# Apple Stocks
# O(n) time
# O(1) space

def get_max_profit(stock_prices):
    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for i in range(len(stock_prices)):
        if i == 0:
            continue

        profit = stock_prices[i] - min_price
        max_profit = max(profit, max_profit)
        min_price = min(stock_prices[i], min_price)

    return max_profit

print get_max_profit([10, 7, 5, 8, 11, 9])
print get_max_profit([10, 7, 5, 2, 1, 0])

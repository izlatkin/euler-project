


def buy_and_sell_stock_twice(prices:list[int]) -> int:
    min_price_so_far, max_profit = max(prices), 0
    first_buy_sell_profit = [0] * len(prices)
    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        max_profit = max(max_profit, price - min_price_so_far)
        first_buy_sell_profit[i] = max_profit

    max_profit_so_far = 0
    for i, price in reversed(list(enumerate(prices[1:]))):
        max_profit_so_far = max(max_profit_so_far, price)
        max_profit = max(max_profit, max_profit_so_far - price + first_buy_sell_profit[i])

    return max_profit

def main():
    print(buy_and_sell_stock_twice([12, 11, 13, 9, 12, 8, 14, 14, 14]))



if __name__ == '__main__':
    main()
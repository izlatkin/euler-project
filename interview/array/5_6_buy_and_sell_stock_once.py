import math


def buy_and_sell_stock_once(A:list[int]) -> int:
    tmp = max([max(A[i:]) - A[i] for i, e in enumerate(A[:-1])])
    return tmp if tmp > 0 else 0


def buy_and_sell_stock_once_optimal(prices:list[int]) -> int:
    min_price_so_far, max_profit = max(prices), 0
    for price in prices:
        max_profit_sell_now = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_now)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit

def main():
    print(buy_and_sell_stock_once([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))
    print(buy_and_sell_stock_once_optimal([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))



if __name__ == '__main__':
    main()
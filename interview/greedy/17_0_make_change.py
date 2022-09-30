def make_chage(money):
    coins = [100, 50, 25, 10, 5, 1]
    num_coins = 0
    for coin in coins:
        num_coins += money // coin
        money %= coin
    return num_coins



def main():
    print(make_chage(19))


if __name__ == '__main__':
    main()
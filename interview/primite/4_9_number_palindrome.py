import math


def is_palindrome_number(x: int) -> bool:
    if x <= 0:
        return x == 0

    number_of_digits = math.floor(math.log10(x)) + 1
    msd_mask = 10 ** (number_of_digits - 1)
    for i in range(number_of_digits // 2):
        if x // msd_mask != x % 10:
            return False
        x %= msd_mask
        x //= 10
        msd_mask //= 100
    return True


def main():
    print(is_palindrome_number(0))
    print(is_palindrome_number(1))
    print(is_palindrome_number(101))
    print(is_palindrome_number(101101))
    print(is_palindrome_number(10))
    print(is_palindrome_number(-1))
    print(is_palindrome_number(1234567890987654321))



if __name__ == '__main__':
    main()
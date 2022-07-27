import functools
import math
import string


def convert_base(s: str, b1: int, b2: int) -> str:
    def int_digit_to_string(d: int) -> str:
        dd = ["A", "B", "C", "D", "E", "F"]
        if d <= 9:
            return str(d)
        else:
            tmp = ord('A')
            return chr(ord('A') + d - 10)

    is_negative = s[0] == '-'
    #num_as_int = functools.reduce(lambda x, c: s * b1 + string.hexdigits.index(c.lower()), s[is_negative:], 0)
    num_as_int = 0
    for i, c in enumerate(s[is_negative:]):
        if ord(c) <= ord('9'):
            r = int(c)
        else:
            r = ord(c) - ord('A') + 10
        num_as_int += r * b1 ** (len(s) - 1 - is_negative - i)

    result = []
    while True:
        if num_as_int < b2:
            result.append(int_digit_to_string(num_as_int))
            break
        result.append(int_digit_to_string(num_as_int % b2))
        num_as_int //= b2

    return "".join(reversed(result))


def ss_decode_col_id(col: str) -> int:
    tmp = lambda result, c: result * 26 + ord(c) - ord('A') + 1, col, 0
    tmp = functools.reduce(tmp)
    return tmp


def main():
    # tests
    #print(convert_base("100", 10, 2))
    #print(convert_base("100", 10, 7))
    #print(convert_base("15", 10, 16))
    print(convert_base("A", 16, 10))
    print(convert_base("FFFFFFF", 16, 10))
    print(ss_decode_col_id("AAAAAAAA"))



if __name__ == '__main__':
    main()
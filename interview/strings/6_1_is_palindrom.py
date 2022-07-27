import math


def is_palindrom(s: str) -> bool:
    return all(s[i] == s[~i] for i in range(len(s) // 2))


def main():
    # tests
    print(is_palindrom("abcba"))
    print(is_palindrom("abcb"))


if __name__ == '__main__':
    main()
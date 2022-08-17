import collections
import functools
import operator


def can_form_palindrome(s: str) -> bool:
    return sum(v % 2 for v in collections.Counter(s).values()) <= 1



def main():
    print(can_form_palindrome('ssss'))
    print(can_form_palindrome('ssvss'))
    print(can_form_palindrome('abc'))




if __name__ == '__main__':
    main()
import functools
import math
import string


def replace_remove(s: str) -> str:
    input = list(s)
    index = 0
    number_of_a = 0
    for c in input:
        if c != 'b':
            input[index] = c
            index += 1
        if c == 'a':
            number_of_a += 1

    number_of_b = len(s) - index
    if number_of_a > number_of_b:
        input += ['a'] * (number_of_a - number_of_b)
    elif number_of_a < number_of_b:
        for _ in range(number_of_b - number_of_a):
            input.pop()

    i = 0
    while i < len(input):
        c = input[index - 1]
        index -= 1
        if c != 'a':
            input[~i] = c
        else:
            input[~i] = 'd'
            input[~(i + 1)] = 'd'
            i += 1
        i +=1

    return "".join(input)


def main():
    # replace aech 'a' by two 'd's
    # delete each entry of 'b'
    # print(replace_remove("acdbbca"))
    print(replace_remove("acdbbcabbbb"))



if __name__ == '__main__':
    main()
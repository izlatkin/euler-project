import functools
import math
import string




def look_and_say(n: int) -> str:
    def next_number(s):
        result, i = [], 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
                count += 1
            result.append(str(count) + s[i])
            i += 1
        return ''.join(result)
    s = '1'
    for _ in range(1, n):
        s = next_number(s)

    return s


def main():
    for i in range(20):
        print(look_and_say(i))



if __name__ == '__main__':
    main()
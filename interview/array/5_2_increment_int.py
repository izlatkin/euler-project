import math


def increment_it(A:list[int]) -> list[int]:
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    else:
        if A[0] == 10:
            A[0] = 0
            A.insert(0, 1)
    return A


def main():
    print(increment_it([1, 2, 3]))
    print(increment_it([9, 9, 9]))
    print(increment_it([2, 9, 9]))
    print(increment_it([1]))
    print(increment_it([9]))
    print(increment_it([1, 2, 3, 9, 9]))



if __name__ == '__main__':
    main()
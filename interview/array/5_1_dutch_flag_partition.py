import math


def is_palidutch_flag_partiotion_o_n_2(pivot_index: int, A: list[int]) -> None:
    if pivot_index > len(A) - 1:
        return
    pivot = A[pivot_index]
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break
    for i in reversed(range(len(A))):
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break


def is_palidutch_flag_partiotion_space(pivot_index: int, A: list[int]) -> None:
    if pivot_index > len(A) - 1:
        return
    pivot = A[pivot_index]
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] > pivot:
            A[larger], A[i] = A[i], A[larger]
            larger -= 1


def is_palidutch_flag_partiotion(pivot_index: int, A: list[int]) -> None:
    if pivot_index > len(A) - 1:
        return
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A) - 1
    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller += 1
            equal += 1
        elif A[equal] == pivot:
            equal += 1
        else: # A[equal] > pivot
            A[larger], A[equal] = A[equal], A[larger]
            larger -= 1


def main():
    A = [1, 3, 2, 2, 1, 1, 1, 3, 3]
    is_palidutch_flag_partiotion_o_n_2(2, A)
    print(A)
    A = [1, 3, 2, 2, 1, 1, 1, 3, 3]
    is_palidutch_flag_partiotion_space(2, A)
    print(A)
    A = [1, 3, 2, 2, 1, 1, 1, 3, 3]
    is_palidutch_flag_partiotion(2, A)
    print(A)
    A = [0] * 10
    is_palidutch_flag_partiotion(2, A)
    print(A)



if __name__ == '__main__':
    main()
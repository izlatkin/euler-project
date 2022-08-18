def merge_two_sorted_arrays(l1: list[int], l2: list[int]) -> list[int]:
    n1, n2 = len(l1), len(l2)
    l1 = l1 + n2 * [0]
    i, j = n1 - 1, n2 - 1
    index = n1 + n2 - 1
    while i >= 0 and j >= 0:
        if l1[i] > l2[j]:
            l1[index] = l1[i]
            i -= 1
        else:
            l1[index] = l2[j]
            j -= 1
        index -= 1
    while j >= 0:
        l1[index] = l2[j]
        index -= 1
        j -= 1
    return l1

def main():
    print(merge_two_sorted_arrays([2, 3, 3, 5, 5, 6, 7, 7, 8, 12], [5, 5, 6, 8, 8, 9, 10, 10]))


if __name__ == '__main__':
    main()
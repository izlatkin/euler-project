def intersection_of_sorted_arrays(l1: list[int], l2: list[int]) -> list[int]:
    result = []
    i , j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] == l2[j]:
            if i == 0 or l1[i] != l1[i - 1]: # to avoid repeated elements
                result.append(l1[i])
            i += 1
            j += 1
        elif l1[i] > l2[j]:
            j += 1
        else: # l1[i] < l2[j]:
            i += 1
    return result


def main():
    print(intersection_of_sorted_arrays([2, 3, 3, 5, 5, 6, 7, 7, 8, 12], [5, 5, 6, 8, 8, 9, 10, 10]))


if __name__ == '__main__':
    main()
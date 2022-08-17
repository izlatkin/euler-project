import heapq
import random

def binary_search(k: int, sample: list[int]) -> int:
    left, right, result = 0, len(sample), -1
    while left <= right:
        mid = (left + right) // 2
        if sample[mid] == k:
            result = mid
            break
        elif sample[mid] > k:
            right = mid - 1
        else:
            left = mid
    return result


def binary_search_left(k: int, sample: list[int]) -> int:
    left, right, result = 0, len(sample), -1
    while left < right:
        mid = (left + right) // 2
        if sample[mid] == k:
            result = mid
            right = mid - 1
        elif sample[mid] > k:
            right = mid - 1
        else:
            left = mid + 1
    return result


def binary_search_right(k: int, sample: list[int]) -> int:
    left, right, result = 0, len(sample), -1
    while left < right:
        mid = min((left + right) // 2, len(sample) - 1)
        if sample[mid] == k:
            result = mid
            left = mid + 1
        elif sample[mid] > k:
            right = mid - 1
        else:
            left = mid + 1
    return result


def find_index(sample: list[int]) -> int:
    left, right = 0, len(sample) - 1
    while left <= right:
        mid = (right + left) // 2
        difference = sample[mid] - mid
        if difference == 0:
            return mid
        elif difference > 0:
            right = mid - 1
        else:
            left = mid + 1
    return -1



def main():
    sample = [1, 1, 1, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7] + 8 * [8] + [10]
    print(sample)
    print(binary_search(4, sample))
    print(binary_search(8, sample))
    print(binary_search_left(4, sample))
    print(binary_search_right(4, sample))
    print(binary_search_left(8, sample))
    print(binary_search(8, sample))
    print(binary_search_right(8, sample))
    print(binary_search_left(10, sample))
    print(binary_search_right(10, sample))

    print(binary_search_left(1, sample))
    print(binary_search(1, sample))
    print(binary_search_right(1, sample))

    sample = [-2, 0, 2, 3, 6, 7, 9]
    print(sample)
    print(find_index(sample))
    sample = [-2, -1, 0, 0, 2, 2, 3]
    print(sample)
    print(find_index(sample))



if __name__ == '__main__':
    main()
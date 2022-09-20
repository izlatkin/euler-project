def find_sum_of_two_my(A, val):
    def binary_search(element, start=0, end=len(A) - 1):
        while start + 1 < end:
            pivot = (start + end) // 2
            if element == A[pivot]:
                return pivot
            elif element < A[pivot]:
                end = pivot
            else:  # element > A[pivot]
                start = pivot
        return -1
    A = sorted(A)  # O(n*log(n))
    for a in A:  # O(n*log(n))
        if binary_search(val - a) != -1:  # O(log(n))
            return [a, val - a]
    return -1;


def find_sum_of_two(A, val):
    found_values = set()
    for a in A:
        if val - a in found_values:
            return [a, val - a]

        found_values.add(a)

    return False


def main():
    print(find_sum_of_two([1,2,3,4,5,6,7,8] , 10))


if __name__ == '__main__':
    main()

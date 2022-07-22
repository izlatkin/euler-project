


def delete_duplicates(A:list[int]) -> int:
    if not A:
        return 0
    unique = 1
    for i in range(1, len(A)):
        if A[unique - 1] != A[i]:
            A[unique] = A[i]
            unique += 1
    return unique


def delete_duplicates_2(A:list[int]) -> int:
    if not A:
        return 0
    duplicates = []
    for i in range(1, len(A)):
        if A[i - 1] == A[i]:
            duplicates.append(i)
    for i in reversed(duplicates):
        A.pop(i)
    return len(A)



def main():
    print(delete_duplicates_2([2, 3, 5, 5, 7, 11, 11, 13]))


if __name__ == '__main__':
    main()
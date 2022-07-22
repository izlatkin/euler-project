


def rearrange(A:list[int]) -> list[int]:
    if len(A) <= 1:
        return A
    if len(A) == 2:
        if A[0] > A[1]:
            A[0], A[1] = A[1], A[0]
        return A
    for i in range(len(A)):
        A[i:i + 2] = sorted(A[i:i + 2], reverse=bool(i % 2))
    return A


def main():
    print(rearrange([12, 11, 13, 9, 12, 8, 14, 14, 14]))



if __name__ == '__main__':
    main()
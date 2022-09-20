import itertools


def get_power(power):
    res, S, A = 0, [0], [0] + power + [0]  # O(N)
    tmp = itertools.accumulate(A) #pre compute sums
    tmp2 = itertools.accumulate(tmp, initial=0) #pre compute sum of sums
    P = list(tmp2)
    for r in range(len(A)):  # O(N)
        while A[S[-1]] > A[r]:  # when min change
            l, i = S[-2], S.pop()
            left = (i - l) * (P[r] - P[i])
            right = (r - i) * (P[i] - P[l])
            res += A[i] * (left - right)
        S.append(r)
    return res % (10 ** 9 + 7)


def main():
    print(get_power([2, 1, 3]))




if __name__ == '__main__':
    main()
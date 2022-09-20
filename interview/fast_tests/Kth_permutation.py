def findFirstNumIndex(k, n):
    if (n == 1):
        return 0, k

    n -= 1

    first_num_index = 0

    # n_actual_fact = n!
    n_partial_fact = n

    while (k >= n_partial_fact and n > 1):
        n_partial_fact = n_partial_fact * (n - 1)
        n -= 1

    # First position of the kth sequence
    # will be occupied by the number present
    # at index = k / (n-1)!
    first_num_index = k // n_partial_fact

    k = k % n_partial_fact

    return first_num_index, k


# Function to find the
# kth permutation of n numbers
def findKthPermutation(n, k):
    # Store final answer
    ans = ""

    s = set()

    # Insert all natural number
    # upto n in set
    for i in range(1, n + 1):
        s.add(i)

    # Subtract 1 to get 0 based indexing
    k = k - 1

    for i in range(n):
        # Mark the first position
        itr = list(s)

        index, k = findFirstNumIndex(k, n - i)

        # itr now points to the
        # number at index in set s
        ans += str(itr[index])

        # remove current number from the set
        itr.pop(index)

        s = set(itr)

    return ans


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def find_kth_permutation(v, k, result):
    if k > factorial(len(v)):
        return
    if not v:
        return
    result = []
    while v:
        f = factorial(len(v) - 1)
        current_index = (k - 1) // f
        result.append(v[current_index])
        k = k % f
        v.remove(v[current_index])
    return result

    # n = len(v)
    # # count is number of permutations starting with first digit
    # count = factorial(n - 1)
    # selected = (k - 1) // count
    #
    # result += str(v[selected])
    # #del v[selected]
    # v.remove(v[selected])
    # k = k - (count * selected)
    # find_kth_permutation(v, k, result)
    # return result


def get_subsets(v, current, results):

    if not current:
        current = []
    for j, e in enumerate(v):
        current.append(e)
        #results.append(current)
        print(current)
        if v[j + 1:]:
            get_subsets(v[j + 1:], current, results)
        current.pop()
    #return results


# Driver code
if __name__ == '__main__':
    n = 3
    k = 4

    kth_perm_seq = findKthPermutation(n, k)

    #print(kth_perm_seq)
    #print(find_kth_permutation([1, 2, 3], 6, []))

    print(get_subsets([1,2,3], [], []))
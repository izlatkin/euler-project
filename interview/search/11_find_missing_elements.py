import collections
import functools
from typing import List


DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                             ('duplicate', 'missing'))


def find_duplicate_missing(A: list[int]) -> DuplicateAndMissing:

    # Compute the XOR of all numbers from 0 to |A| - 1 and all entries in A.
    miss_xor_dup = functools.reduce(lambda v, i: v ^ i[0] ^ i[1], enumerate(A),
                                    0)

    # We need to find a bit that's set to 1 in miss_xor_dup. Such a bit must
    # exist if there is a single missing number and a single duplicated number
    # in A.
    #
    # The bit-fiddling assignment below sets all of bits in differ_bit
    # to 0 except for the least significant bit in miss_xor_dup that's 1.
    differ_bit, miss_or_dup = miss_xor_dup & (~(miss_xor_dup - 1)), 0
    for i, a in enumerate(A):
        # Focus on entries and numbers in which the differ_bit-th bit is 1.
        if i & differ_bit:
            miss_or_dup ^= i
        if a & differ_bit:
            miss_or_dup ^= a

    # miss_or_dup is either the missing value or the duplicated entry.
    # If miss_or_dup is in A, miss_or_dup is the duplicate;
    # otherwise, miss_or_dup is the missing value.
    return (DuplicateAndMissing(miss_or_dup, miss_or_dup
                                ^ miss_xor_dup) if miss_or_dup in A else
            DuplicateAndMissing(miss_or_dup ^ miss_xor_dup, miss_or_dup))


def res_printer(prop, value):
    def fmt(x):
        return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

    return fmt(value)


if __name__ == '__main__':
    tmp = [int(s) for s in "0, 0".split(',')]
    print(find_duplicate_missing(tmp))
    tmp = [int(s) for s in "12, 14, 41, 74, 79, 22, 16, 11, 24, 76, 101, 27, 60, 31, 0, 13, 53, 90, 89, 1, 4, 85, 9, 77, 43, 93, 51, 86, 35, 5, 67, 71, 21, 46, 56, 95, 66, 19, 20, 44, 73, 91, 61, 69, 83, 34, 17, 29, 58, 78, 36, 49, 99, 38, 96, 40, 92, 37, 33, 15, 47, 5, 23, 3, 26, 64, 52, 81, 82, 8, 28, 25, 32, 65, 68, 70, 72, 94, 63, 7, 55, 10, 45, 100, 84, 2, 54, 98, 50, 39, 6, 88, 48, 97, 57, 59, 87, 62, 75, 30, 18, 42".split(',')]
    print(find_duplicate_missing(tmp))
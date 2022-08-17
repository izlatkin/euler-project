import collections

Subarray = collections.namedtuple('Subarray', ('start', 'finish'))

def find_longest_distinct_subarray(paragraph: list[int]):
    recent_occuracy = {} # {word: index}
    result = 0
    longest_dup_free_index = 0
    for i, p in enumerate(paragraph):
        if p in recent_occuracy:
            dup_ind = recent_occuracy[p]
            if dup_ind > longest_dup_free_index:
                result = max(result, i - longest_dup_free_index)
                longest_dup_free_index = dup_ind + 1
        recent_occuracy[p] = i
    return max(result, len(paragraph) - longest_dup_free_index)


def main():
    print(find_longest_distinct_subarray(list("a a b b c a b c c c a a b".split())))
    print(find_longest_distinct_subarray(list("a a b b c a a b c c c a b".split())))


if __name__ == '__main__':
    main()
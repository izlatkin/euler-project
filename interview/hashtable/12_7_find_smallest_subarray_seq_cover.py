import collections

Subarray = collections.namedtuple('Subarray', ('start', 'finish'))

def find_smallest_subarray_seq_cov(paragraph: list[int], keywords: list[int]):
    keywords_to_indx = {k: i for i, k in enumerate(keywords)}
    latest_occurence = [-1] * len(keywords)
    shorterst_sub_array_lenght = [float('inf')] * len(keywords)
    shortest_dist = float('inf')
    result = Subarray(-1, -1)
    for i, p in enumerate(paragraph):
        if p in keywords:
            keyword_indx = keywords_to_indx[p]
            if keyword_indx == 0: # first keyword
                shorterst_sub_array_lenght[keyword_indx] = 1
            elif shorterst_sub_array_lenght[keyword_indx - 1] != float('inf'):
                distance_to_prev_keyword = (i - latest_occurence[keyword_indx - 1])
                shorterst_sub_array_lenght[keyword_indx] = (distance_to_prev_keyword +
                                                            shorterst_sub_array_lenght[keyword_indx -1])
            latest_occurence[keyword_indx] = i
            if (keyword_indx == len(keywords) - 1 and shorterst_sub_array_lenght[-1] < shortest_dist):
                shortest_dist = shorterst_sub_array_lenght[-1]
                result = Subarray(i - shortest_dist + 1, i)
    return result

def main():
    print(find_smallest_subarray_seq_cov(list("a a b b c a b c c c a a b".split()), list("c a b".split())))
    print(find_smallest_subarray_seq_cov(list("a a b b c a a b c c c a b".split()), list("c a b".split())))


if __name__ == '__main__':
    main()
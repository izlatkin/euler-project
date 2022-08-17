import collections


def find_smallest_subarray(paragraph, keywords):
    keywords_to_cover = collections.Counter(keywords)
    result_left, result_right = -1, -1
    remaining_to_cover = len(keywords)
    left = 0
    for right, p in enumerate(paragraph):
        if p in keywords:
            keywords_to_cover[p] -= 1
            if keywords_to_cover[p] >= 0: # ToDo why this condition if needed
                remaining_to_cover -= 1

            while remaining_to_cover == 0:
                if (result_left == -1 and result_right == -1) or (right - left < result_right - result_left):
                    result_left = left
                    result_right = right
                pl = paragraph[left]
                if pl in keywords:
                    keywords_to_cover[pl] += 1
                    if keywords_to_cover[pl] > 0:
                        remaining_to_cover += 1
                left += 1
    return result_left, result_right


def main():
    print(find_smallest_subarray(list("a a b b c a b c c".split()), set("a b c".split())))


if __name__ == '__main__':
    main()
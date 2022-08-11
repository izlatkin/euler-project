import heapq
import random

def merge_sorted_files(sample):
    min_heap: list[tuple[int, int]] = []

    sample_iter = [iter(x) for x in sample]
    for i, it in enumerate(sample_iter):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))

    result = []
    while min_heap:
        smallest_entry, smallest_array_i = heapq.heappop(min_heap)
        smallest_array_iter = sample_iter[smallest_array_i]
        result.append(smallest_entry)
        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_array_i))
    return result


def main():
    sample = [sorted(random.sample(range(0, 30), 5)) for i in range(3)]
    for s in sample:
        print(s)

    print(merge_sorted_files(sample))



if __name__ == '__main__':
    main()
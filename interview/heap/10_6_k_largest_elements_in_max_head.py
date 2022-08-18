import heapq
import random


def k_largest_in_max_heap(data, k):
    results = []
    tmp_heap = []

    heapq.heappush(tmp_heap, (data[0], 0))
    for _ in range(k):
        tmp = heapq.heappop(tmp_heap)
        candidate_index = tmp[1]

        results.append(-tmp[0])

        left_ind, right_ind = candidate_index * 2 + 1, candidate_index * 2 + 2
        if left_ind < len(data):
            heapq.heappush(tmp_heap, (data[left_ind], left_ind))
        if right_ind < len(data):
            heapq.heappush(tmp_heap, (data[right_ind], right_ind))
    return results



def main():
    sample = random.sample(range(0, 20), 11)
    print(sorted(sample))
    test_heap = []
    for s in sample:
        heapq.heappush(test_heap, -s)
    print(test_heap)
    print(k_largest_in_max_heap(test_heap, 3))


if __name__ == '__main__':
    main()
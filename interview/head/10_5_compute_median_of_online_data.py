import heapq
import random


def compute_median_of_online_data(data):
    min_heap = []
    max_heap = []

    result = []
    for x in data:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, x))
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
    print(min_heap)
    print(max_heap)
    return 0.5 * (min_heap[0] + (-max_heap[0])) if len(min_heap) == len(max_heap) else min_heap[0]


def main():
    sample = random.sample(range(0, 20), 11)
    print(sample)
    print(compute_median_of_online_data(sample))




if __name__ == '__main__':
    main()
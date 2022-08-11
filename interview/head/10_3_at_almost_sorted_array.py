import heapq
import random

def equals_array(ar1, ar2):
    if len(ar1) != len(ar2):
        return False
    else:
        for i, a in enumerate(ar1):
            if a != ar2[i]:
                return False
        return True


def sort_approximatry_sorted_array(sample, k):
    min_heap = []
    result = []
    for i in range(k):
        heapq.heappush(min_heap, sample[i])

    for i in range(k, len(sample)):
        smallest = heapq.heappushpop(min_heap, sample[i])
        result.append(smallest)

    while min_heap:
        smallest = heapq.heappop(min_heap)
        result.append(smallest)

    return result


def main():
    sample = sorted(random.sample(range(0, 1000), 100))
    print(sample)
    copy = [s for s in sample]
    # five random swap, k = 5
    for i in range(0, len(sample), len(sample) // 5):
        r = random.randint(0, 5)
        sample[i], sample[i + r] = sample[i + r], sample[i]

    print(sample)
    print(equals_array(copy, sample))

    result = sort_approximatry_sorted_array(sample, 5)
    print(result)

    print(equals_array(copy, result))




if __name__ == '__main__':
    main()
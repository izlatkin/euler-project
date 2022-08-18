import collections
import heapq


def h_citation(citations: list[int]):
    citations.sort() # O(n*log(n))
    n = len(citations)
    for i, c in enumerate(citations): # O(n)
        if c >= n - i:
            return n - i
    return 0


def h_citation_heap(citations: list[int]):
    n = len(citations)
    count_citations = collections.Counter(citations) # O(n)
    hc = []
    for c in count_citations.items(): # O(n)
        heapq.heappush(hc, c)

    sum = 0
    while len(hc) > 0:  # O(n*log(k)) where k is numebr of distinct elemnts
        element, count = heapq.heappop(hc)  # O(log(n))
        sum += count
        if n - sum <= element:
            return element
    return 0


def main():
    print(h_citation([2, 3, 3, 5, 5, 6, 7, 7, 8, 12]))
    print(h_citation_heap([2, 3, 3, 5, 5, 6, 7, 7, 8, 12]))


if __name__ == '__main__':
    main()
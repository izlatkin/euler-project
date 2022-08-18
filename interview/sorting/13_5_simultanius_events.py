import heapq


class Event:

    def __init__(self, start: int, finish: int):
        self.start = start
        self.finish = finish

    def __repr__(self):
        return "start: {} finish {} \n".format(self.start, self.finish)

    def __lt__(self, other):
        return self.start > other.start


def max_simult_events(events: list[Event]):
    events.sort(reverse=True) # 0(n*log(n)) # wost-case O(n**2)
    print(events)

    finish_heap = []
    max_events = 0
    for e in events: # O(n*log(n))
        current_time = e.start
        while finish_heap and finish_heap[0] < current_time: # log(n)
            heapq.heappop(finish_heap)  # log(n)
        heapq.heappush(finish_heap, e.finish) # log(n)
        max_events = max(max_events, len(finish_heap)) # O(1)
    return max_events


def main():
    events = [
        Event(1, 5),
        Event(6, 10),
        Event(11, 13),
        Event(14, 15),
        Event(2, 7),
        Event(8, 9),
        Event(12, 15),
        Event(4, 5),
        Event(9, 17),
        Event(4, 19),
    ]
    print("number of simultaneous events: {}".format(max_simult_events(events)))


if __name__ == '__main__':
    main()
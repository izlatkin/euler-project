import heapq


class Event:

    def __init__(self, start: int, finish: int):
        self.start = start
        self.finish = finish

    def __repr__(self):
        return "start: {} finish {} \n".format(self.start, self.finish)

    def __lt__(self, other):
        return self.start > other.start


def union_invervals(events: list[Event]):
    events.sort(reverse=True) # 0(n*log(n)) # wost-case O(n**2)
    print(events)
    results = []
    current_interval = None
    for e in events:
        if not current_interval:
            current_interval = e
        elif e.start <= current_interval.finish:
            current_interval.finish = max(current_interval.finish, e.finish)
        else:
            results.append(current_interval)
            current_interval = e

    if current_interval:
        results.append(current_interval)
    return results


def main():
    events = [
        Event(1, 3),
        Event(1, 1),
        Event(2, 4),
        Event(3, 4),
        Event(5, 7),
        Event(7, 8),
        Event(8, 11),
        Event(9, 11),
        Event(12, 14),
        Event(12, 16),
        Event(13, 15),
        Event(16, 17)
    ]
    print("union invervals {}".format(union_invervals(events)))
    events = [
        Event(-4, -1),
        Event(0, 2),
        Event(3, 6),
        Event(7, 9),
        Event(11, 12),
        Event(14, 17)
    ]
    print("unio invervals {}".format(union_invervals(events)))


if __name__ == '__main__':
    main()
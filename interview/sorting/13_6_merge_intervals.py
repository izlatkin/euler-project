import heapq


class Event:

    def __init__(self, start: int, finish: int):
        self.start = start
        self.finish = finish

    def __repr__(self):
        return "start: {} finish {} \n".format(self.start, self.finish)

    def __lt__(self, other):
        return self.start > other.start


def merge_invervals(events: list[Event], insert: Event):
    events.sort(reverse=True) # 0(n*log(n)) # wost-case O(n**2)
    print(events)
    result = []
    new_event = Event(insert.start, insert.finish)
    for e in events:
        if e.finish < new_event.start or new_event.finish < e.start:
            result.append(e)
        else:
            if e.start < new_event.start < e.finish:
                new_event.start = e.start
            if e.finish > new_event.finish:
                new_event.finish = e.finish

    index = 0
    for i, r in enumerate(result):
        if e.finish < new_event.start:
            index = i + 1
    #result.append(new_event)
    result.insert(index, new_event )
    return result


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
    print("merged invervals {}".format(merge_invervals(events, Event(5, 10))))
    events = [
        Event(-4, -1),
        Event(0, 2),
        Event(3, 6),
        Event(7, 9),
        Event(11, 12),
        Event(14, 17)
    ]
    print("merged invervals {}".format(merge_invervals(events, Event(1, 8))))


if __name__ == '__main__':
    main()
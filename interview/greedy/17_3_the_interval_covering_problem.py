import collections
import operator


def interval_covering_problem(service_times: list[list[int]]):
    Interval = collections.namedtuple("Interval", ('left', 'right'))
    intervals = [Interval(*s) for s in service_times]
    intervals.sort(key=operator.attrgetter('right'))
    last_visit_time = float('-inf')
    num_visit = 0
    for interval in intervals:
        if interval.left > last_visit_time:
            num_visit += 1
            last_visit_time = interval.right
    return num_visit




def main():
    print(interval_covering_problem([[1, 2], [2, 3], [3, 4], [2, 3], [3, 4], [4, 5]]))


if __name__ == '__main__':
    main()
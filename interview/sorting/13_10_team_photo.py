import heapq


class Event:

    def __init__(self, start: int, finish: int):
        self.start = start
        self.finish = finish

    def __repr__(self):
        return "start: {} finish {} \n".format(self.start, self.finish)

    def __lt__(self, other):
        return self.start > other.start


def validate_placment_exist(team1: list[int], team2: list[int]) -> bool:
    return all(a < b for a, b in zip(sorted(team1), sorted(team2)))


def main():
    team1 = [1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    team2 = [x + 1 for x in team1]
    print(validate_placment_exist(team1, team2))
    print(validate_placment_exist(team1, team1))
    team3 = [1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
    print(validate_placment_exist(team1, team3))
    teamX = [1, 1, 2, 2, 2, 5]
    teamY = [1, 1, 2, 3, 2, 3, 5, 6 ,6]
    print(validate_placment_exist(teamY, teamX))

    result = [a * b for a, b in zip(teamX, teamY)]
    print(result)


if __name__ == '__main__':
    main()
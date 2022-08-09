


def sunset(buildings: str) -> list[int]:
    buildings = list(reversed([int(b) for b in buildings.split()]))
    #print(buildings)
    candidants = []
    for i, h in enumerate(buildings):
        for c in candidants:
            (j, height) = c
            if height < h:
                candidants.remove(c)
        candidants.append((i, h))
    return candidants



def main():
    print(sunset("1 3 2 4 2"))


if __name__ == '__main__':
    main()

def can_reach_end(A:list[int]) -> bool:
    toDo = [0]
    for t in toDo:
        if t + A[t] >= len(A):
            return True
        elif t + A[t] in toDo:
            continue
        else:
            for i in range(1, A[t] + 1):
                toDo.append(t + i)
    return False

def can_reach_end_2(A:list[int]) -> bool:
    toDo = [0]
    while toDo:
        t = toDo.pop(0)
        if t + A[t] >= len(A):
            return True
        elif t + A[t] in toDo:
            continue
        else:
            for i in range(1, A[t] + 1):
                toDo.append(t + i)
    return False


def main():
    print(can_reach_end([3, 3, 1, 0, 2, 0, 1]))
    print(can_reach_end([3, 2, 0, 0, 2, 0, 1]))
    print(can_reach_end([0]))
    print(can_reach_end([1]))
    print(can_reach_end([1, 1, 1, 1, 1]))
    print(can_reach_end([5, 0, 0, 0, 0]))
    print(can_reach_end([2, 0, 2, 0, 0]))
    print(can_reach_end([2, 0, 2, 0, 1]))

    print(can_reach_end_2([3, 3, 1, 0, 2, 0, 1]))
    print(can_reach_end_2([3, 2, 0, 0, 2, 0, 1]))
    print(can_reach_end_2([0]))
    print(can_reach_end_2([1]))
    print(can_reach_end_2([1, 1, 1, 1, 1]))
    print(can_reach_end_2([5, 0, 0, 0, 0]))
    print(can_reach_end_2([2, 0, 2, 0, 0]))
    print(can_reach_end_2([2, 0, 2, 0, 1]))



if __name__ == '__main__':
    main()
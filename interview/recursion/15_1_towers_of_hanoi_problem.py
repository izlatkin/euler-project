def towers_of_hanoi_problem(num_rings):
    def towers_of_hanoi_problem_helper(num_to_move, from_peg, to_pef, use_peg):
        if num_to_move > 0:
            towers_of_hanoi_problem_helper(num_to_move - 1, from_peg, use_peg, to_pef)
            tmp = pegs[from_peg][-1]
            pegs[to_pef].append(pegs[from_peg].pop())
            result.append([from_peg, to_pef, tmp])
            towers_of_hanoi_problem_helper(num_to_move - 1, use_peg, to_pef, from_peg)

    result = []
    pegs = [list(reversed(range(1, num_rings + 1)))] + [[]] + [[]]
    print(pegs)
    towers_of_hanoi_problem_helper(num_rings, 0, 1, 2)
    print(len(result))
    # for r in result:
    #     print(r)


def main():
    print(towers_of_hanoi_problem(20))


if __name__ == '__main__':
    main()
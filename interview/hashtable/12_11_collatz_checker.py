import collections

def test_collatz_conjecture(n: int) -> bool:
    verify_numbers = {1: [1], 2: [2, 1]}
    for i in range(3, n + 1):
        sequence = set()
        sequence_list = []
        curr_value = i
        while curr_value >= i:
            if curr_value in sequence:
                return False
            sequence_list.append(curr_value)
            sequence.add(curr_value)
            if curr_value % 2 == 1: # odd case
                if curr_value in verify_numbers:
                    verify_numbers[i] = sequence_list + verify_numbers[curr_value]
                    break
                curr_value = 3 * curr_value + 1
            else:
                curr_value //= 2
        if i not in verify_numbers:
            verify_numbers[i] = sequence_list + verify_numbers[curr_value]

    [print(i) for i in verify_numbers.items()]
    print(max(len(i[1]) for i in verify_numbers.items()))
    return True



def main():
    print(test_collatz_conjecture(10000))


if __name__ == '__main__':
    main()
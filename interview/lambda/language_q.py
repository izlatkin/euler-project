import heapq
import random


def test1():
    increment_by_i = [lambda x: x + i for i in range(10)]
    print(increment_by_i[3](1))
    print(increment_by_i[3](4))
    print(increment_by_i[3](0))
    print(increment_by_i[3](-100))
    print(increment_by_i[0](0))
    print(increment_by_i[3](0))
    print(increment_by_i[0](0))

    example = lambda x: x + 10
    print(example(1))


    example2 = lambda x, y: [x + y, x - y]
    test1 = example2(2, 1)
    print(test1)


def test2():
    sample = random.sample(range(0, 100), 60)
    it = iter(sample)
    tmp = next(it, '-1')
    while tmp != '-1':
        print(tmp, end=' ')
        tmp = next(it, '-1')



def main():
    test1()
    test2()


if __name__ == '__main__':
    main()
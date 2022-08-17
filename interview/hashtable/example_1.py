import functools
import operator


def string_hash(s: str, modules: int) -> int:
    mult = 997
    return functools.reduce(lambda v, c: (v * mult + ord(c)) % modules, s, 0)


def string_hash_2(s: str, modules: int) -> int:
    mult = 997
    hf = lambda v, c: (v * mult + ord(c)) % modules

    tmp = [hf(v, c) for v, c in enumerate(s)]

    return sum(tmp)



def main():
    print(string_hash('ssss', 10000))
    print(string_hash_2('ssss', 10000))

    lis = [1, 3, 5, 6, 2, ]
    print(functools.reduce(operator.add, lis))

    dictinaty = {'a':3, 'b': 4}
    sstet = set()
    sstet.add('a')
    sstet.add('b')
    sstet.remove('a')
    sstet.discard('a')

    print(sstet)
    #dictinaty.discard()



if __name__ == '__main__':
    main()
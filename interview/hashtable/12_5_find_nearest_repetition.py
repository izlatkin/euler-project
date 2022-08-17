
def find_nearest_repetition(paragraph) -> int:
    paragraph = [p.lower() for p in paragraph]
    dictinary = dict()
    for i, p in enumerate(paragraph):
        if p not in dictinary:
            dictinary[p] = (i, 0)
        else:
            index, lenght = dictinary[p]
            if lenght == 0:
                dictinary[p] = (i, i - index)
            else:
                dictinary[p] = (i, min(i - index, lenght))
    tmp = [lenght[1][1] for lenght in dictinary.items() if lenght[1][1] != 0]
    return min(tmp)




def main():
    print(find_nearest_repetition(list("a b c a b c c".split())))
    print(find_nearest_repetition(list("a b c d e f b e".split())))






if __name__ == '__main__':
    main()
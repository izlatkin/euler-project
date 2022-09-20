def noPrefix(words):
    # Write your code here
    checked = dict()
    for i, w in enumerate(words):
        checked[w] = i
    m = len(words) + 1
    for i, w in enumerate(words):
        for j in range(len(w) ):
            if w[:j] in checked:
                m = min(m, max(i, checked[w[:j]]))

    if m != -1:
        print("BED SET")
        print(words[m])
    else:
        print("GOOD SET")


def main():
    words = [l.strip('\n') for l in open('words.txt', 'r').readlines()]
    noPrefix(words)



if __name__ == '__main__':
    main()
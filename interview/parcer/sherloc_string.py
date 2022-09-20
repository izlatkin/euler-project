def isValid(s):
    sd = dict()
    for c in s:
        if c in sd:
            sd[c] += 1
        else:
            sd[c] = 1

    if len(sd) == 1:
        return "YES"

    print(sd)

    counts_dict = dict()
    for k in sd:
        if sd[k] in counts_dict:
            counts_dict[sd[k]] += 1
        else:
            counts_dict[sd[k]] = 1
    print(counts_dict)

    if len(counts_dict) > 2:
        return "NO"
    elif len(counts_dict) == 1:
        return "YES"
    else:
        a, b = counts_dict.items()
        if a[1] != 1:
            a, b = b, a
        return "YES" if a[0] - b[0] == 1 or (a[0] == 1 and a[1] == 1) else "NO"

def main():
    f = open("sherloc.txt", 'r').readlines()
    print(isValid(f[0].strip()))




if __name__ == '__main__':
    main()
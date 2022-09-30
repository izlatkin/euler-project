def all_mnemonics(phone_number):
    def all_mnemonics_helper(index):
        if index == len(spn):
            mnemonics.append(''.join(dump))
        else:
            for c in MAP[int(spn[index])]:
                dump[index] = c
                all_mnemonics_helper(index + 1)


    MAP = ['0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    spn = str(phone_number)
    dump = ['0'] * len(spn)
    mnemonics = []
    all_mnemonics_helper(0)
    print(mnemonics)


def main():
    print(all_mnemonics(9042078810))


if __name__ == '__main__':
    main()
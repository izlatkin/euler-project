
# Test 1 : MMDCLXVI

def encode(s: str) -> None:
    current = 1
    prev = s[0]
    results = []
    for c in s[1:]:
        if c == prev:
            current += 1
        else:
            results.append("{}{}".format(current, prev))
            prev = c
            current = 1
    results.append("{}{}".format(current, prev))
    print(''.join(results))


def decode(s: str) -> None:
    result = []
    for i in range(len(s) // 2):
        result.append(s[2 * i + 1] * int(s[2 * i]))
    print(''.join(result))





def main():
    encode('aaabcccaa')
    decode('3e4f2e')

if __name__ == '__main__':
    main()
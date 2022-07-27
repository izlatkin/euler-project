
# Test 1 : MMDCLXVI



def roman_to_decimal(s: str) -> str:
    ROMAN ={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    current = ROMAN[s[0].upper()]
    sum = 0
    prev = s[0]
    for c in s[1:].upper():
        if c == prev:
            current += ROMAN[c]
        else:
            if ROMAN[prev] > ROMAN[c]:
                sum += current
            else:
                sum -= current
            current = ROMAN[c]
            prev = c

    if current != 0:
        sum += current

    return sum


def main():
    print(roman_to_decimal('IIII'))
    print(roman_to_decimal('V'))
    print(roman_to_decimal('MMDCLXVI'))
    print(roman_to_decimal('IV'))
    print(roman_to_decimal('IIV'))
    print(roman_to_decimal('IIIV'))



if __name__ == '__main__':
    main()
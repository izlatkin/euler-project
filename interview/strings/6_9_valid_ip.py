
# Test 1 : MMDCLXVI

def is_valid(s):
    if not s:
        return False
    return (len(s) == 1 and s[0] != '0') or (s[0] != '0' and int(s) <= 255)


def valid_ip(s: str, result = [], iter = 0):
    if iter >= 3:
        if is_valid(s):
            to_print = '.'.join(result) + "." + s
            print(to_print)
        return

    for i in range(0, min(len(s), 3)):
        if is_valid(s[:i + 1]):
            valid_ip(s[i + 1:], result + [s[:i + 1]], iter + 1)



def main():
    valid_ip('19216811')
    valid_ip('255255255255')
    valid_ip('255255255256')
    valid_ip('1111')



if __name__ == '__main__':
    main()
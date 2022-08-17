import collections

def find_all_substrings(s: str, words: list[int]):
    wsize = sum(len(w) for w in words)
    unit_size = len(words[0])
    word_to_freq = collections.Counter(words)
    for start in range(0, len(s) - 1 - wsize):
        curr_string_to_freq = collections.Counter()
        flag = False
        for i in range(start, start + wsize, unit_size):
            curr_word = s[i:i + unit_size]
            it = word_to_freq[curr_word]
            if it == 0:
                flag = True
                break
            curr_string_to_freq[curr_word] += 1
            if curr_string_to_freq[curr_word] > it:
                flag = True
                break
        if not flag:
            return True
    return False


def main():
    print(find_all_substrings("njdfkvndfacbdcmkls", list("a b c".split())))
    print(find_all_substrings("njdfkvndfacbdcmklsdcba",list("a b c d".split())))
    print(find_all_substrings("njdfkvndfacbdcmklsdcba", list("a b c x".split())))


if __name__ == '__main__':
    main()
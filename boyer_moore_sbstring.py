def shift_sz(pattern, missmatch_char, pattern_idx):
    shift = 0
    while pattern[pattern_idx] != missmatch_char:
        shift += 1
        pattern_idx -= 1
        if pattern_idx < 0:
            return len(pattern) - 1
    return shift

def boyers_moore(text, pattern):
    # check if empy text
    if len(text) < len(pattern):
        raise StopIteration

    text_idx = len(pattern) - 1
    patt_idx = len(pattern) - 1

    while text_idx < len(text):
        for i in range(0, len(pattern)):
            if pattern[patt_idx - i] != text[text_idx - i]:
                text_idx += shift_sz(pattern, text[text_idx - i], patt_idx - i)
                break
            if i == patt_idx:
                yield text_idx - len(pattern) + 1
                text_idx += 1

if __name__ == "__main__":
    main_string = "gcttctgctaccttttgcgcgcgcgcggaaccttttgc"
    pattern =     "ccttttgc"
    for i in boyers_moore(main_string, pattern):
        print(i)
    
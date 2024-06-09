
def get_median_string(s, t):
    all_strings = []
    for i in range(ord('a'), ord('a') + 26):
        for j in range(ord('a'), ord('a') + 26):
            if i != j and chr(i) != s[0] and chr(j) != t[0]:
                all_strings.append(chr(i) + chr(j))
    all_strings.sort()
    return all_strings[len(all_strings) // 2]


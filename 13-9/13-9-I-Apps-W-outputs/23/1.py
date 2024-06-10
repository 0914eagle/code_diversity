
def is_good(s):
    count_zeros = 0
    count_ones = 0
    for c in s:
        if c == '0':
            count_zeros += 1
        else:
            count_ones += 1
    return count_zeros != count_ones

def find_good_substrings(s):
    if len(s) == 1:
        return [s]
    for i in range(1, len(s)):
        if is_good(s[:i]) and is_good(s[i:]):
            return [s[:i], s[i:]]
    return None

def solve(s):
    k = 1
    while True:
        substrings = find_good_substrings(s)
        if substrings is not None:
            return k, substrings
        k += 1

if __name__ == '__main__':
    n = int(input())
    s = input()
    k, substrings = solve(s)
    print(k)
    print(*substrings, sep=' ')



def is_good(s):
    count_zeros = 0
    count_ones = 0
    for c in s:
        if c == '0':
            count_zeros += 1
        else:
            count_ones += 1
    return count_zeros != count_ones

def cut_into_good_substrings(s):
    if is_good(s):
        return [s]

    for i in range(1, len(s)):
        if is_good(s[:i]) and is_good(s[i:]):
            return [s[:i], s[i:]]

    return None

def main():
    n = int(input())
    s = input()
    result = cut_into_good_substrings(s)
    if result is None:
        print(-1)
    else:
        print(len(result))
        for s in result:
            print(s, end=' ')

if __name__ == '__main__':
    main()


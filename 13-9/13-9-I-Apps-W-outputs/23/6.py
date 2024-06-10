
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
    if not is_good(s):
        return [s]
    else:
        i = 1
        while i < len(s) and is_good(s[:i]):
            i += 1
        return [s[:i-1]] + cut_into_good_substrings(s[i-1:])

def main():
    n = int(input())
    s = input()
    k = len(cut_into_good_substrings(s))
    print(k)
    for s in cut_into_good_substrings(s):
        print(s, end=' ')

if __name__ == '__main__':
    main()


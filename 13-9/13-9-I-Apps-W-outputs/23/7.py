
def is_good_string(s):
    count_zeros = 0
    count_ones = 0
    for c in s:
        if c == '0':
            count_zeros += 1
        else:
            count_ones += 1
    return count_zeros != count_ones

def cut_string(s):
    if not is_good_string(s):
        return []
    if len(s) == 1:
        return [s]
    for i in range(1, len(s)):
        if is_good_string(s[:i]) and is_good_string(s[i:]):
            return [s[:i]] + cut_string(s[i:])
    return []

def main():
    n = int(input())
    s = input()
    result = cut_string(s)
    print(len(result))
    print(' '.join(result))

if __name__ == '__main__':
    main()


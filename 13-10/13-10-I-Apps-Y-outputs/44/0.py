
def is_subsequence(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)

def remove_substring(s, t):
    max_length = 0
    for i in range(len(s)):
        if is_subsequence(s[:i] + s[i+1:], t):
            max_length = max(max_length, i+1)
    return max_length

def main():
    s = input()
    t = input()
    print(remove_substring(s, t))

if __name__ == '__main__':
    main()


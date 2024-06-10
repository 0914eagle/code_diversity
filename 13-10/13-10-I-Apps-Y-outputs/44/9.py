
def is_subsequence(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)

def remove_substring(s, t):
    max_len = 0
    for i in range(len(s)):
        if s[i] == t[0]:
            j = 1
            while i+j < len(s) and j < len(t) and s[i+j] == t[j]:
                j += 1
            if j == len(t):
                max_len = max(max_len, j)
    return max_len

def main():
    s = input()
    t = input()
    if is_subsequence(s, t):
        print(remove_substring(s, t))
    else:
        print("-1")

if __name__ == '__main__':
    main()


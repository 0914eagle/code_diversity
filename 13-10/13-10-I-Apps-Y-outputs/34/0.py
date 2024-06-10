
def get_substrings(s, k):
    n = len(s)
    substrings = 0
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if all(c in substring for c in k):
                substrings += 1
    return substrings

def get_available_substrings(s, k):
    n = len(s)
    substrings = 0
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if all(c in substring for c in k):
                substrings += 1
    return substrings

if __name__ == '__main__':
    n, k = map(int, input().split())
    s = input()
    k = set(input().split())
    print(get_available_substrings(s, k))


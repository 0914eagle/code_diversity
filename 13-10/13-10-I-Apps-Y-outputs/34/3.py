
def get_substrings(s, k):
    n = len(s)
    substrings = 0
    for i in range(n):
        for j in range(i, n):
            if all(c in k for c in s[i:j+1]):
                substrings += 1
    return substrings

def get_available_substrings(s, k):
    n = len(s)
    substrings = 0
    for i in range(n):
        for j in range(i, n):
            if all(c in k for c in s[i:j+1]):
                substrings += 1
    return substrings

if __name__ == '__main__':
    n, k = map(int, input().split())
    s = input()
    k = set(map(int, input().split()))
    print(get_available_substrings(s, k))


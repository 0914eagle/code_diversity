
def get_substrings(s, k):
    n = len(s)
    substrings = 0
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if all(c in k for c in substring):
                substrings += 1
    return substrings

def main():
    n, k = map(int, input().split())
    s = input()
    k = set(input().split())
    print(get_substrings(s, k))

if __name__ == '__main__':
    main()


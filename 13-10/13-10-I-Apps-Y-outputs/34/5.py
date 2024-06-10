
def get_substrings(s, k):
    substrings = []
    for i in range(len(s)):
        for j in range(i, len(s) + 1):
            substring = s[i:j]
            if all(c in k for c in substring):
                substrings.append(substring)
    return substrings

def count_substrings(s, k):
    return len(get_substrings(s, k))

def main():
    n, k = map(int, input().split())
    s = input()
    k = set(input())
    print(count_substrings(s, k))

if __name__ == '__main__':
    main()



def get_substrings(s, k):
    substrings = []
    for i in range(len(s)):
        for j in range(i, len(s) + 1):
            substring = s[i:j]
            if all(c in k for c in substring):
                substrings.append(substring)
    return substrings

def get_usable_substrings(s, k):
    substrings = get_substrings(s, k)
    usable_substrings = []
    for substring in substrings:
        if all(c in k for c in substring):
            usable_substrings.append(substring)
    return usable_substrings

def main():
    n, k = map(int, input().split())
    s = input()
    k = set(input().split())
    print(len(get_usable_substrings(s, k)))

if __name__ == '__main__':
    main()


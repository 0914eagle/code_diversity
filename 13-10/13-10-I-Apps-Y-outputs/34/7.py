
def get_available_substrings(s, k):
    substrings = []
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if all(c in substring for c in k):
                substrings.append(substring)
    return substrings

def count_available_substrings(s, k):
    return len(get_available_substrings(s, k))

def main():
    n, k = map(int, input().split())
    s = input()
    k = set(input().split())
    print(count_available_substrings(s, k))

if __name__ == '__main__':
    main()


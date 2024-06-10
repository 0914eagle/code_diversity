
def get_substrings(s, k):
    substrings = []
    for i in range(len(s)):
        for j in range(i, len(s) + 1):
            substring = s[i:j]
            if all(letter in k for letter in substring):
                substrings.append(substring)
    return substrings

def count_usable_substrings(s, k):
    return len(get_substrings(s, k))

if __name__ == '__main__':
    n, k = map(int, input().split())
    s = input()
    k = set(input())
    print(count_usable_substrings(s, k))


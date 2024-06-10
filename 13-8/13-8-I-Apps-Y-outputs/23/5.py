
def get_substrings(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if substring not in substrings:
                substrings.append(substring)
    return substrings

def kth_lexicographically_smallest_substring(s, k):
    substrings = get_substrings(s)
    substrings.sort()
    return substrings[k-1]

if __name__ == '__main__':
    s = input()
    k = int(input())
    print(kth_lexicographically_smallest_substring(s, k))


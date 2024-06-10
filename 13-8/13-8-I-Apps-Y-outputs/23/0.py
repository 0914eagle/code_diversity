
def get_substrings(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substrings.append(s[i:j])
    return substrings

def get_kth_lexicographically_smallest_substring(s, k):
    substrings = get_substrings(s)
    substrings.sort()
    return substrings[k-1]

if __name__ == '__main__':
    s = input()
    k = int(input())
    print(get_kth_lexicographically_smallest_substring(s, k))


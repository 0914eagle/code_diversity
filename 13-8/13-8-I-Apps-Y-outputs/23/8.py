
import sys

def get_substrings(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substrings.append(s[i:j])
    return substrings

def kth_lexicographically_smallest(s, k):
    substrings = get_substrings(s)
    substrings.sort()
    return substrings[k-1]

def main():
    s = sys.stdin.readline().strip()
    k = int(sys.stdin.readline().strip())
    print(kth_lexicographically_smallest(s, k))

if __name__ == '__main__':
    main()



def f1(n, s):
    # Find the longest alternating subsequence of the string
    longest_alternating_subsequence = 0
    for i in range(n):
        current_subsequence = 0
        for j in range(i, n):
            if s[i] != s[j]:
                current_subsequence += 1
            else:
                break
        longest_alternating_subsequence = max(longest_alternating_subsequence, current_subsequence)
    return longest_alternating_subsequence

def f2(n, s):
    # Find the longest alternating subsequence of the string after flipping a single substring
    longest_alternating_subsequence = 0
    for i in range(n):
        for j in range(i+1, n+1):
            flipped_substring = s[:i] + ''.join('1' if c == '0' else '0' for c in s[i:j]) + s[j:]
            current_subsequence = 0
            for k in range(i, j):
                if flipped_substring[k] != flipped_substring[k-1]:
                    current_subsequence += 1
            longest_alternating_subsequence = max(longest_alternating_subsequence, current_subsequence)
    return longest_alternating_subsequence

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(f2(n, s))


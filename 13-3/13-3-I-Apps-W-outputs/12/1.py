
def solve(s):
    n = len(s)
    # Initialize the maximum length of the longest non-decreasing subsequence as 0
    max_len = 0
    # Initialize the substring with the maximum number of zeroes as an empty string
    max_substring = ""
    # Iterate over all possible substrings
    for i in range(n):
        for j in range(i, n):
            # Check if the substring is non-decreasing
            if is_non_decreasing(s[i:j+1]):
                # Check if the length of the substring is greater than the current maximum length
                if len(s[i:j+1]) > max_len:
                    # Update the maximum length and the substring with the maximum number of zeroes
                    max_len = len(s[i:j+1])
                    max_substring = s[i:j+1]
    return max_substring

def is_non_decreasing(s):
    # Check if the substring is non-decreasing
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            return False
    return True

s = "010"
print(solve(s))



import sys

def solve(n, s, a):
    # Calculate the maximum length of a substring
    max_len = max(a)

    # Initialize the number of ways to split the message
    num_ways = 0

    # Initialize the longest substring length
    longest_substring = 0

    # Initialize the minimum number of substrings
    min_substrings = sys.maxsize

    # Iterate over all possible split positions
    for i in range(n):
        # Get the substring starting from position i
        substring = s[i:]

        # Check if the substring is valid
        if is_valid_substring(substring, a):
            # Increment the number of ways to split the message
            num_ways += 1

            # Update the longest substring length
            longest_substring = max(longest_substring, len(substring))

            # Update the minimum number of substrings
            min_substrings = min(min_substrings, count_substrings(substring))

    # Return the number of ways to split the message, the longest substring length, and the minimum number of substrings
    return num_ways % (10**9 + 7), longest_substring, min_substrings

def is_valid_substring(substring, a):
    # Check if the substring is empty
    if not substring:
        return True

    # Get the first character of the substring
    first_char = substring[0]

    # Get the maximum length of the first character
    max_len = a[ord(first_char) - ord('a')]

    # Check if the substring is longer than the maximum length
    if len(substring) > max_len:
        return False

    # Recursively check if the remaining substring is valid
    return is_valid_substring(substring[1:], a)

def count_substrings(s):
    # Initialize the number of substrings
    num_substrings = 0

    # Iterate over all possible split positions
    for i in range(len(s)):
        # Increment the number of substrings
        num_substrings += 1

    # Return the number of substrings
    return num_substrings

n = int(input())
s = input()
a = list(map(int, input().split()))
print(*solve(n, s, a))


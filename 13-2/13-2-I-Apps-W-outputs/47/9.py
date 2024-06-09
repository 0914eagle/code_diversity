
import sys

def count_ways(n, s, a):
    # Initialize the number of ways to be 0
    ways = 0
    
    # Loop through each substring of length 1 to n
    for i in range(1, n + 1):
        # Get the number of substrings of length i
        num_substrings = n // i
        
        # Loop through each substring of length i
        for j in range(num_substrings):
            # Get the start index of the substring
            start = j * i
            
            # Check if the substring is valid
            if is_valid_substring(s[start:start + i], a):
                # Increment the number of ways
                ways += 1
    
    # Return the number of ways modulo 10^9 + 7
    return ways % 1000000007

def is_valid_substring(s, a):
    # Initialize the maximum length of a substring to be 0
    max_len = 0
    
    # Loop through each character in the substring
    for c in s:
        # Get the index of the character in the alphabet
        index = ord(c) - ord('a')
        
        # Check if the length of the substring is valid
        if a[index] < len(s):
            return False
        
        # Update the maximum length of the substring
        max_len = max(max_len, a[index])
    
    # Return True if the substring is valid
    return True

def get_longest_substring(n, s, a):
    # Initialize the longest substring to be empty
    longest_substring = ""
    
    # Loop through each substring of length 1 to n
    for i in range(1, n + 1):
        # Get the number of substrings of length i
        num_substrings = n // i
        
        # Loop through each substring of length i
        for j in range(num_substrings):
            # Get the start index of the substring
            start = j * i
            
            # Check if the substring is valid
            if is_valid_substring(s[start:start + i], a):
                # Update the longest substring
                longest_substring = max(longest_substring, s[start:start + i])
    
    # Return the length of the longest substring
    return len(longest_substring)

def get_min_substrings(n, s, a):
    # Initialize the minimum number of substrings to be infinity
    min_substrings = sys.maxsize
    
    # Loop through each substring of length 1 to n
    for i in range(1, n + 1):
        # Get the number of substrings of length i
        num_substrings = n // i
        
        # Loop through each substring of length i
        for j in range(num_substrings):
            # Get the start index of the substring
            start = j * i
            
            # Check if the substring is valid
            if is_valid_substring(s[start:start + i], a):
                # Update the minimum number of substrings
                min_substrings = min(min_substrings, num_substrings)
    
    # Return the minimum number of substrings
    return min_substrings

n = int(input())
s = input()
a = list(map(int, input().split()))

print(count_ways(n, s, a))
print(get_longest_substring(n, s, a))
print(get_min_substrings(n, s, a))


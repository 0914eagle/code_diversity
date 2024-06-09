
import sys

def count_ways(n, s, a):
    # Initialize the number of ways to split the message
    num_ways = 0
    
    # Initialize the longest substring length
    longest_substring = 0
    
    # Initialize the minimum number of substrings
    min_substrings = sys.maxsize
    
    # Loop through each substring of the message
    for i in range(n):
        # Get the length of the current substring
        curr_len = 1
        
        # Loop through the remaining substring
        for j in range(i+1, n):
            # Check if the current substring is valid
            if s[j] not in s[i:j] and curr_len <= a[ord(s[j]) - ord('a')]:
                # Increment the length of the current substring
                curr_len += 1
            else:
                # Break the loop if the current substring is not valid
                break
        
        # Check if the current substring is valid
        if curr_len == n:
            # Increment the number of ways to split the message
            num_ways += 1
            
            # Update the longest substring length
            longest_substring = max(longest_substring, curr_len)
            
            # Update the minimum number of substrings
            min_substrings = min(min_substrings, curr_len)
    
    # Return the number of ways to split the message, the longest substring length, and the minimum number of substrings
    return num_ways, longest_substring, min_substrings

n = int(input())
s = input()
a = list(map(int, input().split()))

num_ways, longest_substring, min_substrings = count_ways(n, s, a)

print(num_ways % (10**9 + 7))
print(longest_substring)
print(min_substrings)


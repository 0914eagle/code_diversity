
def get_substring_length(s, k):
    # Initialize variables
    n = len(s)
    count = 0
    i = 0
    j = 0
    
    # Loop through the string
    while i < n and j < k:
        # If the current character is 'R', 'G', or 'B', increment the count
        if s[i] in ["R", "G", "B"]:
            count += 1
            j += 1
        i += 1
    
    # Return the count
    return count

def solve(s, k):
    # Initialize variables
    n = len(s)
    min_changes = n
    i = 0
    
    # Loop through the string
    while i < n:
        # If the current character is 'R', 'G', or 'B', check if the substring starting from this position is a substring of the infinite string "RGBRGBRGB ..."
        if s[i] in ["R", "G", "B"]:
            # Get the length of the substring
            substring_length = get_substring_length(s[i:], k)
            # If the substring is long enough, update the minimum number of changes
            if substring_length >= k:
                min_changes = min(min_changes, n - substring_length)
        i += 1
    
    # Return the minimum number of changes
    return min_changes

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        n, k = map(int, input().split())
        s = input()
        print(solve(s, k))


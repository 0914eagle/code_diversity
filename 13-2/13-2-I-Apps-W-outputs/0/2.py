
def solve(s):
    # Initialize variables
    n = len(s)
    count = 0
    complementary_pairs = {"A": "T", "T": "A", "C": "G", "G": "C"}
    
    # Iterate through each substring of length 2 to n
    for i in range(n):
        for j in range(i+1, n+1):
            # Check if the substring is complementary
            if is_complementary(s[i:j], complementary_pairs):
                count += 1
    
    return count

def is_complementary(s, complementary_pairs):
    # Check if the string is complementary
    for i in range(len(s)):
        if s[i] != complementary_pairs[s[i]]:
            return False
    return True


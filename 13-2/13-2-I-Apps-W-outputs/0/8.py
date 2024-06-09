
def solve(s):
    # Initialize variables
    n = len(s)
    count = 0
    complementary_pairs = {"A": "T", "T": "A", "C": "G", "G": "C"}
    
    # Iterate through each substring of length 2 to n
    for i in range(n):
        for j in range(i+1, n+1):
            # Extract substring
            substring = s[i:j]
            
            # Check if substring is complementary
            if is_complementary(substring, complementary_pairs):
                count += 1
    
    return count

def is_complementary(substring, complementary_pairs):
    # Initialize variables
    n = len(substring)
    complementary = True
    
    # Iterate through each character of substring
    for i in range(n):
        # Check if character is complementary
        if substring[i] != complementary_pairs[substring[n-i-1]]:
            complementary = False
            break
    
    return complementary


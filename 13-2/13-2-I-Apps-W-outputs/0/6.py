
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
    # Check if substring is empty
    if len(substring) == 0:
        return False
    
    # Check if substring is complementary
    for i in range(len(substring)):
        if substring[i] != complementary_pairs[substring[i]]:
            return False
    
    return True

if __name__ == "__main__":
    n = int(input())
    s = input()
    print(solve(s))


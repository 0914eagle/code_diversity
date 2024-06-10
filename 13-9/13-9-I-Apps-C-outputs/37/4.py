
def is_perfect(s):
    # Check if s is a subset of the powers of 2
    if not set(s).issubset(set(range(1 << len(s)))):
        return False
    
    # Check if s is a perfect set
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] ^ s[j] not in s:
                return False
    return True

def count_perfect_sets(k):
    # Initialize a set to store the perfect sets
    perfect_sets = set()
    
    # Iterate from 0 to k and check if each number is a perfect set
    for i in range(k + 1):
        if is_perfect(set(range(i + 1))):
            perfect_sets.add(i)
    
    # Return the number of perfect sets
    return len(perfect_sets)

if __name__ == '__main__':
    k = int(input())
    print(count_perfect_sets(k) % 1000000007)


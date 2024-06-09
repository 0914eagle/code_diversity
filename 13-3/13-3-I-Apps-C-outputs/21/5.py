
def get_wcd(pairs):
    # Initialize a set to store the common divisors
    common_divisors = set()
    
    # Iterate over the pairs
    for a, b in pairs:
        # Get the common divisors of a and b
        divisors = set(range(2, min(a, b) + 1))
        
        # Intersect the common divisors with the previous set
        common_divisors &= divisors
    
    # If the set is empty, return -1
    if not common_divisors:
        return -1
    
    # Return the largest element in the set
    return max(common_divisors)

def main():
    n = int(input())
    pairs = []
    
    for i in range(n):
        a, b = map(int, input().split())
        pairs.append((a, b))
    
    print(get_wcd(pairs))

if __name__ == '__main__':
    main()


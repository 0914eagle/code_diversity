
def get_magical_permutation(n, s):
    # Initialize a list to store the magical permutation
    permutation = []
    
    # Iterate from 0 to 2^n - 1
    for i in range(2**n):
        # Check if the current number is a magical number
        if is_magical_number(i, n, s):
            # If it is, add it to the permutation
            permutation.append(i)
    
    # Return the permutation
    return permutation

def is_magical_number(num, n, s):
    # Check if the number is a power of 2
    if num == 0 or num & (num - 1) != 0:
        return False
    
    # Iterate from 0 to n - 1
    for i in range(n):
        # Check if the bitwise xor of the current number and the previous number is in the set S
        if (num >> i) ^ (num >> (i + 1)) not in s:
            return False
    
    # If all conditions are met, return True
    return True

def main():
    # Read the input
    n = int(input())
    s = set(map(int, input().split()))
    
    # Get the magical permutation
    permutation = get_magical_permutation(n, s)
    
    # Print the result
    print(len(permutation))
    print(*permutation)

if __name__ == '__main__':
    main()


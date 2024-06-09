
def get_magical_permutation(n, s):
    # Initialize a list to store the magical permutation
    permutation = []
    
    # Iterate from 0 to 2^n - 1
    for i in range(2**n):
        # Initialize a variable to store the bitwise xor of the current element and the previous element
        xor = 0
        
        # Iterate through the set of integers
        for j in range(n):
            # Calculate the bitwise xor of the current element and the previous element
            xor ^= (i >> j) & 1
            
            # If the bitwise xor is in the set of integers, add it to the permutation
            if xor in s:
                permutation.append(xor)
                break
    
    # Return the magical permutation
    return permutation

def main():
    # Read the input n and set s
    n = int(input())
    s = set(map(int, input().split()))
    
    # Find the largest non-negative integer x such that there is a magical permutation of integers from 0 to 2^x - 1
    x = 0
    while get_magical_permutation(x, s) == []:
        x += 1
    
    # Print the largest non-negative integer x and the magical permutation
    print(x)
    print(*get_magical_permutation(x, s))

if __name__ == '__main__':
    main()


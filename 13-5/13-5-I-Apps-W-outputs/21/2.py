
def get_permutation(b_prime, c_prime):
    # Initialize an empty list to store the permutation
    permutation = []
    
    # Loop through each element of b_prime and c_prime
    for i in range(len(b_prime)):
        # If the current element of b_prime is less than the current element of c_prime, append the index of the current element of b_prime to the permutation
        if b_prime[i] < c_prime[i]:
            permutation.append(i)
        # Otherwise, append the index of the current element of c_prime to the permutation
        else:
            permutation.append(i + 1)
    
    # Return the permutation
    return permutation

def get_array(permutation, n):
    # Initialize an empty list to store the array
    array = []
    
    # Loop through each element of the permutation
    for i in range(n):
        # If the current element of the permutation is not equal to the previous element of the permutation, append the current element of the permutation to the array
        if i == 0 or permutation[i] != permutation[i - 1]:
            array.append(permutation[i])
    
    # Return the array
    return array

def main():
    # Read the input from stdin
    n = int(input())
    b_prime = list(map(int, input().split()))
    c_prime = list(map(int, input().split()))
    
    # Get the permutation from the input arrays
    permutation = get_permutation(b_prime, c_prime)
    
    # Get the array from the permutation
    array = get_array(permutation, n)
    
    # Print the array
    print(*array)

if __name__ == '__main__':
    main()



def get_permutation_index(permutation, size):
    # Calculate the factorial of the size
    factorial = 1
    for i in range(2, size+1):
        factorial *= i
    
    # Initialize the index
    index = 0
    
    # Iterate through the permutation and calculate the index
    for i in range(size):
        # Calculate the number of permutations before the current element
        num_permutations = factorial // (size-i)
        
        # Calculate the index of the current element
        index += permutation[i] * num_permutations
        
        # Update the factorial
        factorial = factorial // (size-i)
    
    return index

def get_lexicographically_smaller_index(permutation1, permutation2, size):
    # Get the indices of the permutations
    index1 = get_permutation_index(permutation1, size)
    index2 = get_permutation_index(permutation2, size)
    
    # Return the absolute difference between the indices
    return abs(index1 - index2)

def main():
    # Read the input
    size = int(input())
    permutation1 = list(map(int, input().split()))
    permutation2 = list(map(int, input().split()))
    
    # Calculate the absolute difference between the indices
    answer = get_lexicographically_smaller_index(permutation1, permutation2, size)
    
    # Print the answer
    print(answer)

if __name__ == '__main__':
    main()


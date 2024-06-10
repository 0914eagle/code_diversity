
def get_lexicographically_smallest_permutation(permutation):
    # Calculate the number of permutations of size N
    num_permutations = 1
    for i in range(1, len(permutation) + 1):
        num_permutations *= i
    
    # Initialize the lexicographically smallest permutation as the first permutation
    lexicographically_smallest_permutation = permutation
    
    # Loop through each permutation and check if it is lexicographically smaller than the current smallest permutation
    for i in range(1, num_permutations):
        current_permutation = list(permutation)
        current_permutation.sort()
        if current_permutation < lexicographically_smallest_permutation:
            lexicographically_smallest_permutation = current_permutation
    
    return lexicographically_smallest_permutation

def get_lexicographically_largest_permutation(permutation):
    # Calculate the number of permutations of size N
    num_permutations = 1
    for i in range(1, len(permutation) + 1):
        num_permutations *= i
    
    # Initialize the lexicographically largest permutation as the last permutation
    lexicographically_largest_permutation = permutation
    
    # Loop through each permutation and check if it is lexicographically larger than the current largest permutation
    for i in range(1, num_permutations):
        current_permutation = list(permutation)
        current_permutation.sort()
        if current_permutation > lexicographically_largest_permutation:
            lexicographically_largest_permutation = current_permutation
    
    return lexicographically_largest_permutation

def get_absolute_difference(permutation1, permutation2):
    # Get the lexicographically smallest and largest permutations of both permutations
    smallest_permutation1 = get_lexicographically_smallest_permutation(permutation1)
    largest_permutation1 = get_lexicographically_largest_permutation(permutation1)
    smallest_permutation2 = get_lexicographically_smallest_permutation(permutation2)
    largest_permutation2 = get_lexicographically_largest_permutation(permutation2)
    
    # Calculate the absolute difference between the lexicographically smallest and largest permutations of both permutations
    absolute_difference = abs(smallest_permutation1 - largest_permutation2) + abs(smallest_permutation2 - largest_permutation1)
    
    return absolute_difference

if __name__ == '__main__':
    # Read the input from stdin
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    
    # Calculate the absolute difference between the permutations
    absolute_difference = get_absolute_difference(P, Q)
    
    # Print the result
    print(absolute_difference)


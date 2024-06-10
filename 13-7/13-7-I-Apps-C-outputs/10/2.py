
def get_candy_distribution(a, b):
    # Initialize the distribution dictionary
    distribution = {}
    
    # Loop through the candy values
    for i in range(len(a)):
        # Check if the candy is liked by both siblings
        if a[i] == b[i]:
            # If so, add it to the distribution dictionary with value 'A'
            distribution[i] = 'A'
        # Check if the candy is liked by only one sibling
        elif a[i] != b[i] and a[i] != 0 and b[i] != 0:
            # If so, add it to the distribution dictionary with value 'B'
            distribution[i] = 'B'
    
    # Return the distribution dictionary
    return distribution

def get_candy_distribution_lexicographically_smallest(a, b):
    # Get the candy distribution
    distribution = get_candy_distribution(a, b)
    
    # Initialize the lexicographically smallest distribution
    lexicographically_smallest_distribution = ''
    
    # Loop through the candy values
    for i in range(len(a)):
        # Add the candy value to the lexicographically smallest distribution
        lexicographically_smallest_distribution += distribution[i]
    
    # Return the lexicographically smallest distribution
    return lexicographically_smallest_distribution

if __name__ == '__main__':
    # Get the number of candies
    n = int(input())
    
    # Get the candy values
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # Get the lexicographically smallest candy distribution
    distribution = get_candy_distribution_lexicographically_smallest(a, b)
    
    # Print the lexicographically smallest candy distribution
    print(distribution)


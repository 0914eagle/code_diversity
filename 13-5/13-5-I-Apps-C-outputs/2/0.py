
def get_candy_distribution(a, b):
    # Initialize the distribution dictionary
    distribution = {}
    
    # Loop through the candies and assign them to the sibling with the highest value
    for i in range(len(a)):
        if a[i] >= b[i]:
            distribution[i] = "A"
        else:
            distribution[i] = "B"
    
    # Return the distribution dictionary
    return distribution

def get_candy_distribution_lexicographically_smallest(a, b):
    # Initialize the distribution dictionary
    distribution = {}
    
    # Loop through the candies and assign them to the sibling with the highest value
    for i in range(len(a)):
        if a[i] >= b[i]:
            distribution[i] = "A"
        else:
            distribution[i] = "B"
    
    # Sort the distribution dictionary by key
    sorted_distribution = sorted(distribution.items(), key=lambda x: x[0])
    
    # Return the distribution dictionary as a string
    return "".join([item[1] for item in sorted_distribution])

def main():
    # Read the input
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # Call the functions
    distribution = get_candy_distribution(a, b)
    lexicographically_smallest_distribution = get_candy_distribution_lexicographically_smallest(a, b)
    
    # Print the output
    print(lexicographically_smallest_distribution)

if __name__ == '__main__':
    main()


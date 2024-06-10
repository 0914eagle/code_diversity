
def get_shortest_test_scheme(k, allergens):
    # Sort the allergens by their live duration in descending order
    allergens = sorted(allergens, reverse=True)
    
    # Initialize the number of days as the sum of the live durations of all allergens
    num_days = sum(allergens)
    
    # Iterate through the allergens and subtract the live duration of each allergen that is applied in the morning
    for i in range(k):
        num_days -= allergens[i]
    
    # Return the number of days
    return num_days

def main():
    # Read the number of allergens and their live durations from stdin
    k = int(input())
    allergens = [int(input()) for _ in range(k)]
    
    # Call the get_shortest_test_scheme function and print the result
    print(get_shortest_test_scheme(k, allergens))

if __name__ == '__main__':
    main()


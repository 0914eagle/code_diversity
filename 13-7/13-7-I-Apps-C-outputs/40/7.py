
def get_shortest_test_scheme(k, durations):
    # Sort the durations in non-decreasing order
    durations.sort()
    
    # Initialize the number of days needed for the test scheme
    num_days = 0
    
    # Iterate through the durations and add the number of days needed for each allergen
    for duration in durations:
        num_days += duration
    
    # Return the number of days needed for the test scheme
    return num_days

def main():
    # Read the number of allergens and their durations from stdin
    k = int(input())
    durations = []
    for i in range(k):
        durations.append(int(input()))
    
    # Call the get_shortest_test_scheme function and print the result
    print(get_shortest_test_scheme(k, durations))

if __name__ == '__main__':
    main()


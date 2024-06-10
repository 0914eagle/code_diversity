
def get_shortest_test_scheme(k, durations):
    # Sort the durations in non-decreasing order
    durations.sort()
    
    # Initialize the number of days needed for the test scheme
    num_days = 0
    
    # Loop through each allergen and add its duration to the number of days needed for the test scheme
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


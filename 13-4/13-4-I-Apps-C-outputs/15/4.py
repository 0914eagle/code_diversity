
def get_shortest_test_scheme(k, durations):
    # Sort the durations in non-decreasing order
    durations.sort()
    
    # Initialize the number of days needed for the test scheme
    num_days = 0
    
    # Iterate through the durations and add the number of days needed for each allergen
    for duration in durations:
        num_days += duration
    
    # Return the total number of days needed for the test scheme
    return num_days

def main():
    # Read the number of allergens and their live durations from stdin
    k = int(input())
    durations = []
    for i in range(k):
        durations.append(int(input()))
    
    # Call the function to get the shortest test scheme
    num_days = get_shortest_test_scheme(k, durations)
    
    # Print the number of days needed for the test scheme
    print(num_days)

if __name__ == '__main__':
    main()


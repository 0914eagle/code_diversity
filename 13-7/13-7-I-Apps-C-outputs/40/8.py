
def get_shortest_test_scheme(k, durations):
    # Sort the durations in non-decreasing order
    durations.sort()
    
    # Initialize the number of days as the sum of the durations
    num_days = sum(durations)
    
    # Loop through each duration and check if it can be removed without affecting the test outcome
    for i in range(k):
        # Remove the current duration and check if the number of days is still sufficient
        num_days -= durations[i]
        if num_days >= k:
            # If the number of days is still sufficient, continue with the next duration
            continue
        else:
            # If the number of days is not sufficient, return the current number of days
            return num_days + 1
    
    # If all durations have been removed, return the total number of days
    return num_days

def main():
    k = int(input())
    durations = []
    for i in range(k):
        durations.append(int(input()))
    print(get_shortest_test_scheme(k, durations))

if __name__ == '__main__':
    main()


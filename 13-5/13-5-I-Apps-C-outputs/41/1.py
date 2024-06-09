
def get_min_rest_days(n, a):
    # Initialize variables
    rest_days = 0
    last_day_sport = -1
    last_day_contest = -1
    
    # Iterate through the days
    for i in range(n):
        # Check if the gym is open and a contest is carried out
        if a[i] in [2, 3]:
            # Check if the last day was a sport day
            if last_day_sport == i-1:
                # Increment the number of rest days
                rest_days += 1
            # Update the last day information
            last_day_sport = i
            last_day_contest = i
        # Check if the gym is closed and a contest is carried out
        elif a[i] == 1:
            # Check if the last day was a contest day
            if last_day_contest == i-1:
                # Increment the number of rest days
                rest_days += 1
            # Update the last day information
            last_day_sport = i
            last_day_contest = i
    
    # Return the minimum number of rest days
    return rest_days

def main():
    # Read the input
    n = int(input())
    a = list(map(int, input().split()))
    
    # Call the function to get the minimum number of rest days
    rest_days = get_min_rest_days(n, a)
    
    # Print the result
    print(rest_days)

if __name__ == '__main__':
    main()


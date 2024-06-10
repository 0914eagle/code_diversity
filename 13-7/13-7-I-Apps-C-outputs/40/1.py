
def get_shortest_test_scheme(k, durations):
    # Sort the durations in descending order
    durations.sort(reverse=True)
    
    # Initialize the number of days as the sum of the durations
    num_days = sum(durations)
    
    # Loop through each duration and subtract it from the number of days
    for duration in durations:
        num_days -= duration
        
        # If the number of days is divisible by the duration, return the number of days
        if num_days % duration == 0:
            return num_days // duration
    
    # If no duration is divisible by the number of days, return the number of days
    return num_days

def main():
    k = int(input())
    durations = []
    for i in range(k):
        durations.append(int(input()))
    print(get_shortest_test_scheme(k, durations))

if __name__ == '__main__':
    main()


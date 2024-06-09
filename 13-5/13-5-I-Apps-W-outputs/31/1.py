
def get_min_jury_size(olympiads):
    # Initialize a set to store the dates when the jury is working
    jury_dates = set()
    # Iterate over the olympiads
    for month, day, people, time in olympiads:
        # Get the start and end dates for the current olympiad
        start_date = f"{month}/{day}"
        end_date = f"{month}/{day + time - 1}"
        # Check if the jury is already working on some other olympiad during this period
        if any(date in jury_dates for date in [start_date, end_date]):
            # If the jury is already working, increase the minimum jury size by 1
            people += 1
        # Add the dates when the jury is working to the set
        jury_dates.update([start_date, end_date])
    # Return the minimum jury size
    return people

def main():
    # Read the number of olympiads
    n = int(input())
    # Read the olympiads
    olympiads = []
    for _ in range(n):
        month, day, people, time = map(int, input().split())
        olympiads.append((month, day, people, time))
    # Get the minimum jury size
    min_jury_size = get_min_jury_size(olympiads)
    # Print the minimum jury size
    print(min_jury_size)

if __name__ == '__main__':
    main()


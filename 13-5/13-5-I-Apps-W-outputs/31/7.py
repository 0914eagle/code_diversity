
def get_min_jury_size(olympiads):
    # Initialize a set to store the dates when the jury is working
    jury_dates = set()
    # Iterate over the olympiads
    for month, day, people, time in olympiads:
        # Get the start and end dates for the olympiad
        start_date = f"{month}/{day}"
        end_date = f"{month}/{day + time - 1}"
        # Check if the jury is working on any date within the olympiad duration
        for date in range(int(start_date), int(end_date) + 1):
            # If the date is already in the set, return False
            if date in jury_dates:
                return False
        # Add the dates to the set
        jury_dates.update(range(int(start_date), int(end_date) + 1))
    # If all dates are covered, return True
    return True

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
    # Print the result
    print(min_jury_size)

if __name__ == '__main__':
    main()


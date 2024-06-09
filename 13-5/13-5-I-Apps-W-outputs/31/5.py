
def get_minimum_jury_size(olympiads):
    # Initialize a set to store the dates when the jury is working
    jury_dates = set()
    # Iterate over the olympiads
    for month, day, people, time in olympiads:
        # Get the start and end dates for the olympiad
        start_date = f"{month}/{day}"
        end_date = f"{month}/{day + time - 1}"
        # Check if the jury is working on any date between the start and end dates
        for date in range(int(start_date), int(end_date) + 1):
            if date in jury_dates:
                # If the jury is working on a date between the start and end dates, return False
                return False
        # Add the start and end dates to the set of jury dates
        jury_dates.add(int(start_date))
        jury_dates.add(int(end_date))
    # If the jury is not working on any date between the start and end dates, return True
    return True

def main():
    # Read the number of olympiads
    n = int(input())
    # Read the olympiads
    olympiads = []
    for _ in range(n):
        month, day, people, time = map(int, input().split())
        olympiads.append((month, day, people, time))
    # Call the function to get the minimum jury size
    minimum_jury_size = get_minimum_jury_size(olympiads)
    # Print the result
    print(minimum_jury_size)

if __name__ == '__main__':
    main()


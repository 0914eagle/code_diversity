
def get_minimum_jury_size(olympiads):
    # Initialize a set to store the dates when the jury is working
    jury_dates = set()
    # Iterate over the olympiads
    for month, day, people, time in olympiads:
        # Get the start and end dates for the olympiad
        start_date = f"{month}/{day}"
        end_date = (datetime.strptime(start_date, "%m/%d") + timedelta(days=time-1)).strftime("%m/%d")
        # Add the dates to the set
        jury_dates.update([start_date, end_date])
    # Return the size of the jury
    return len(jury_dates)

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


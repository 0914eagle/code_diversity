
def get_min_jury_size(olympiads):
    # Initialize a set to store the dates when the jury is working
    jury_dates = set()
    # Iterate over the olympiads
    for olympiad in olympiads:
        # Get the month and day of the olympiad
        month, day = olympiad[0], olympiad[1]
        # Get the number of jury members and the preparation time
        num_jury, preparation_time = olympiad[2], olympiad[3]
        # Iterate over the preparation time
        for i in range(preparation_time):
            # Get the date of the preparation
            date = (month, day - i)
            # Add the date to the set of jury dates
            jury_dates.add(date)
    # Return the length of the jury dates set, which is the minimum jury size
    return len(jury_dates)

def main():
    # Read the number of olympiads
    num_olympiads = int(input())
    # Read the olympiads
    olympiads = []
    for i in range(num_olympiads):
        olympiads.append(list(map(int, input().split())))
    # Get the minimum jury size
    min_jury_size = get_min_jury_size(olympiads)
    # Print the minimum jury size
    print(min_jury_size)

if __name__ == '__main__':
    main()


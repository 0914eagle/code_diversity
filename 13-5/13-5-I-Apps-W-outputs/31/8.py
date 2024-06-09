
def get_minimum_jury_size(olympiads):
    # Initialize a set to store the dates when jury members are working
    jury_dates = set()
    # Iterate over the olympiads
    for olympiade in olympiads:
        # Get the month, day, number of jury members, and preparation time for the current olympiade
        month, day, jury_size, preparation_time = olympiade
        # Iterate over the preparation time
        for i in range(preparation_time):
            # Get the date of the preparation day
            preparation_date = (month, day + i)
            # Check if the date is valid
            if preparation_date[1] > days_in_month(preparation_date[0]):
                # If the date is not valid, move to the next day
                preparation_date = (month, 1)
            # Add the date to the set of jury dates
            jury_dates.add(preparation_date)
    # Return the size of the jury needed to prepare all olympiads
    return len(jury_dates)

def days_in_month(month):
    # A list of days in each month
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Return the number of days in the given month
    return days_in_months[month - 1]

if __name__ == '__main__':
    # Read the number of olympiads
    n = int(input())
    # Read the olympiads
    olympiads = []
    for i in range(n):
        month, day, jury_size, preparation_time = map(int, input().split())
        olympiads.append((month, day, jury_size, preparation_time))
    # Call the function to get the minimum jury size
    minimum_jury_size = get_minimum_jury_size(olympiads)
    # Print the result
    print(minimum_jury_size)


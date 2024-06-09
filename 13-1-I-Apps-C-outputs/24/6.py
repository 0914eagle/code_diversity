
def get_schedule(z, f, forbidden_dates):
    # Initialize a dictionary to store the surprise penalty for each date
    surprise_penalty = {}

    # Loop through all possible dates in the given range
    for year in range(2019, 2019 + z):
        for day in range(1, 32):
            # Check if the date is a Friday
            if day % 7 == 5:
                # Check if the date is a Canadian Thanksgiving date
                if (year, 10, day) in forbidden_dates:
                    continue

                # Calculate the surprise penalty for the date
                if year == 2018:
                    surprise_penalty[(year, 10, day)] = 0
                else:
                    surprise_penalty[(year, 10, day)] = (day - 12) ** 2

    # Initialize a list to store the chosen dates
    chosen_dates = []

    # Loop through the dates in chronological order and add them to the list
    for date in sorted(surprise_penalty):
        if surprise_penalty[date] == min(surprise_penalty.values()):
            chosen_dates.append(date)

    # Return the smallest total surprise penalty and the chosen dates
    return min(surprise_penalty.values()), chosen_dates



def get_schedule(Z, F, forbidden_dates):
    # Initialize a list to store the chosen dates
    schedule = []
    
    # Loop through each year from 2019 to 2018 + Z
    for year in range(2019, 2018 + Z + 1):
        # Check if the year is a leap year
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            # If the year is a leap year, add an extra day to the number of days in October
            days_in_october = 31 + 1
        else:
            # If the year is not a leap year, the number of days in October is 31
            days_in_october = 31
        
        # Loop through each day in October
        for day in range(1, days_in_october + 1):
            # Check if the current day is a Friday
            if day % 7 == 5:
                # If the current day is a Friday, check if it is a forbidden date
                if (year, 10, day) in forbidden_dates:
                    # If the current day is a forbidden date, continue to the next day
                    continue
                # If the current day is not a forbidden date, add it to the schedule
                schedule.append((year, 10, day))
                # Break out of the inner loop to move on to the next year
                break
    
    # Return the schedule
    return schedule


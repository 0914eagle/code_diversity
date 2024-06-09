
def solve(cows_per_day, num_days):
    # Initialize a list to store the number of farms to inspect on each day
    farms_to_inspect = [0] * (num_days + 1)

    # Loop through each day and calculate the number of farms to inspect
    for day in range(1, num_days + 1):
        # Calculate the total number of cows on all farms on this day
        total_cows = sum(cows_per_day[:day])

        # Calculate the number of farms with at least one cow on this day
        num_farms = len([cow for cow in cows_per_day[:day] if cow > 0])

        # Calculate the number of farms to inspect on this day
        farms_to_inspect[day] = num_farms + total_cows // 2

    return farms_to_inspect


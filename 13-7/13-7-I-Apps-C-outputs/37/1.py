
def solve(gigs, venues, roads, time):
    # Initialize a dictionary to store the maximum amount of money that can be earned at each venue
    max_money = {}
    for venue in range(1, venues + 1):
        max_money[venue] = 0

    # Loop through each gig and calculate the maximum amount of money that can be earned by playing it
    for gig in gigs:
        venue, start_time, end_time, money = gig
        if start_time <= time <= end_time:
            max_money[venue] = max(max_money[venue], money)

    # Return the maximum amount of money that can be earned by playing any gig
    return max(max_money.values())


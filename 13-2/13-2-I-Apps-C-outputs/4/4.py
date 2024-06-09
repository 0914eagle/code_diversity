
def solve(gigs, venues, roads, time):
    # Initialize a dictionary to store the maximum amount of cryptocents that can be earned at each venue
    max_cryptocents = {venue: 0 for venue in range(1, venues + 1)}

    # Loop through each gig and calculate the maximum amount of cryptocents that can be earned by playing it
    for gig in gigs:
        venue, start_time, end_time, cryptocents = gig
        max_cryptocents[venue] = max(max_cryptocents[venue], cryptocents)

    # Initialize a variable to store the maximum amount of cryptocents that can be earned by playing gigs
    max_gig_cryptocents = 0

    # Loop through each venue and calculate the maximum amount of cryptocents that can be earned by playing gigs at that venue
    for venue in range(1, venues + 1):
        max_gig_cryptocents += max_cryptocents[venue]

    return max_gig_cryptocents


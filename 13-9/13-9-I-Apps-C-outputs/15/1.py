
def solve(n, a):
    # Sort the bids in non-decreasing order
    a.sort()
    # Initialize the minimum bid as the first bid
    min_bid = a[0]
    # Initialize the number of players who have not yet made their bid equal to the minimum bid as the number of players minus 1
    num_players_left = n - 1
    # Iterate through the bids
    for i in range(1, n):
        # If the current bid is not equal to the minimum bid, the player has not yet made their bid equal to the minimum bid
        if a[i] != min_bid:
            # Calculate the number of times the player can double and triple their bid to make their bid equal to the minimum bid
            num_doubles = (a[i] - min_bid) // (2 * min_bid)
            num_triples = (a[i] - min_bid) // (3 * min_bid)
            # If the player can make their bid equal to the minimum bid by doubling and tripling their bid, subtract the number of doubles and triples from the number of players who have not yet made their bid equal to the minimum bid
            num_players_left -= num_doubles + num_triples
    # If all players have made their bid equal to the minimum bid, return "Yes", otherwise return "No"
    if num_players_left == 0:
        return "Yes"
    else:
        return "No"



def solve(n, d, e):
    # Initialize the minimum number of rubles to n
    min_rubles = n
    # Iterate over the possible number of dollar bills
    for i in range(0, n//d+1):
        # Calculate the number of rubles left after buying i dollar bills
        rubles_left = n - i*d
        # If the number of rubles left is divisible by e, we can buy some euro bills
        if rubles_left % e == 0:
            # Calculate the number of euro bills that can be bought
            num_euro = rubles_left // e
            # Calculate the total number of rubles after buying euro bills
            total_rubles = i*d + num_euro*e
            # Update the minimum number of rubles if necessary
            min_rubles = min(min_rubles, total_rubles)
    return min_rubles


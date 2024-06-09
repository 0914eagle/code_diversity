
def solve(n, d, e):
    # Initialize the minimum number of rubles to n
    min_rubles = n
    # Iterate over the possible number of dollar bills
    for i in range(0, n // d + 1):
        # Calculate the number of rubles left after buying i dollar bills
        rubles_left = n - i * d
        # If the number of rubles left is divisible by e, we can buy some euro bills
        if rubles_left % e == 0:
            # Calculate the number of euro bills that can be bought
            num_euro = rubles_left // e
            # If the number of euro bills is less than the minimum, update the minimum
            if num_euro < min_rubles:
                min_rubles = num_euro
    return min_rubles


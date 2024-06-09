
def solve(n, d, e):
    # Initialize the minimum number of rubles to infinity
    min_rubles = float('inf')
    # Iterate over all possible combinations of dollar and euro bills
    for dollar_bills in range(0, n // d + 1):
        for euro_bills in range(0, n // e + 1):
            # Calculate the total number of rubles after exchange
            total_rubles = dollar_bills * d + euro_bills * e
            # If the total number of rubles is less than the minimum, update the minimum
            if total_rubles < min_rubles:
                min_rubles = total_rubles
    # Return the minimum number of rubles
    return min_rubles


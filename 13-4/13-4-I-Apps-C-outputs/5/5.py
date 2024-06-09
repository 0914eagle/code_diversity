
def solve(n, d, e):
    # Initialize the minimum number of rubles to n
    min_rubles = n
    # Iterate over all possible combinations of dollar and euro bills
    for dollar_bill in [1, 2, 5, 10, 20, 50, 100]:
        for euro_bill in [5, 10, 20, 50, 100, 200]:
            # Calculate the total number of rubles after exchanging dollar and euro bills
            total_rubles = dollar_bill * d + euro_bill * e
            # If the total number of rubles is less than the minimum, update the minimum
            if total_rubles < min_rubles:
                min_rubles = total_rubles
    # Return the minimum number of rubles
    return min_rubles


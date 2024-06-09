
def solve(n, m, k, x, s, a, b, c, d):
    # Initialize the minimum time to prepare n potions as the initial time
    min_time = x
    # Loop through all possible combinations of spells
    for i in range(1 << m):
        # Initialize the number of mana points spent as 0
        mana_spent = 0
        # Initialize the number of potions prepared as 0
        potions_prepared = 0
        # Loop through all bits in the current combination
        for j in range(m):
            # Check if the j-th bit is set in the current combination
            if i & (1 << j):
                # If the j-th bit is set, use the j-th spell of the first type
                mana_spent += b[j]
                x = a[j]
        # Loop through all bits in the current combination
        for j in range(k):
            # Check if the j-th bit is set in the current combination
            if i & (1 << (m + j)):
                # If the j-th bit is set, use the j-th spell of the second type
                mana_spent += d[j]
                potions_prepared += c[j]
        # Check if the total number of mana points spent is less than or equal to the maximum allowed
        if mana_spent <= s:
            # Calculate the total time to prepare the required number of potions
            total_time = x * (n - potions_prepared) + potions_prepared * x
            # Update the minimum time if necessary
            min_time = min(min_time, total_time)
    # Return the minimum time
    return min_time


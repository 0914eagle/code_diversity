
def solve(n, m, k, x, s, a, b, c, d):
    # Initialize the minimum time to prepare n potions as infinity
    min_time = float('inf')
    # Loop through all possible combinations of spells
    for i in range(1 << m):
        # Initialize the number of manapoints spent as 0
        mana_spent = 0
        # Initialize the number of potions prepared as 0
        potions_prepared = 0
        # Loop through all bits in the current combination
        for j in range(m):
            # Check if the j-th bit is set in the current combination
            if i & (1 << j):
                # Add the cost of the j-th spell to the total mana spent
                mana_spent += b[j]
                # Add the number of potions created by the j-th spell to the total number of potions prepared
                potions_prepared += c[j]
        # Check if the total number of mana spent is less than or equal to the maximum allowed
        if mana_spent <= s:
            # Calculate the total time to prepare the potions
            total_time = potions_prepared * x
            # Loop through all bits in the current combination
            for j in range(m):
                # Check if the j-th bit is set in the current combination
                if i & (1 << j):
                    # Add the time saved by the j-th spell to the total time
                    total_time -= a[j] * (potions_prepared - c[j])
            # Check if the total time is less than or equal to the minimum time
            if total_time <= min_time:
                # Update the minimum time
                min_time = total_time
    # Return the minimum time
    return min_time


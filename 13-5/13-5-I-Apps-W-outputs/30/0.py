
def solve(n, m, k, x, s, a, b, c, d):
    # Initialize the minimum time to prepare n potions as the initial time
    min_time = x
    # Loop through all possible combinations of spells
    for i in range(1 << m):
        # Initialize the number of mana points spent as 0
        mana_spent = 0
        # Initialize the number of potions prepared as 0
        potions_prepared = 0
        # Loop through all spells
        for j in range(m):
            # Check if the j-th spell is used in the current combination
            if i & (1 << j):
                # Add the cost of the spell to the total mana spent
                mana_spent += b[j]
                # Change the preparation time to a[j]
                x = a[j]
        # Loop through all spells of the second type
        for j in range(k):
            # Check if the j-th spell of the second type is used in the current combination
            if i & (1 << (m + j)):
                # Add the cost of the spell to the total mana spent
                mana_spent += d[j]
                # Add the number of potions created by the spell to the total number of potions prepared
                potions_prepared += c[j]
        # Check if the total mana spent is less than or equal to the maximum mana allowed
        if mana_spent <= s:
            # Calculate the total time to prepare the potions
            time = x * (n - potions_prepared) + potions_prepared * x
            # Update the minimum time if the current combination is faster
            min_time = min(min_time, time)
    # Return the minimum time to prepare n potions
    return min_time


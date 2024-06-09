
def solve(n, m, k, x, s, a, b, c, d):
    # Initialize the minimum time to prepare n potions as the initial preparation time
    min_time = x
    # Loop through all possible combinations of spells
    for i in range(1 << m):
        # Initialize the number of manapoints spent as 0
        mana_spent = 0
        # Initialize the number of potions prepared as 0
        potions_prepared = 0
        # Loop through all spells
        for j in range(m):
            # Check if the j-th spell is used in the current combination
            if i & (1 << j):
                # Add the mana cost of the spell to the total mana spent
                mana_spent += b[j]
                # Change the preparation time to the new value
                x = a[j]
        # Loop through all spells of the second type
        for j in range(k):
            # Check if the j-th spell is used in the current combination
            if i & (1 << (m + j)):
                # Add the mana cost of the spell to the total mana spent
                mana_spent += d[j]
                # Add the number of potions created by the spell to the total number of potions prepared
                potions_prepared += c[j]
        # Check if the total number of mana spent is less than or equal to the maximum allowed
        if mana_spent <= s:
            # Calculate the total time spent on preparing the potions
            time_spent = x * (n - potions_prepared) + potions_prepared * x
            # Update the minimum time if the current combination is faster
            min_time = min(min_time, time_spent)
    # Return the minimum time needed to prepare n potions
    return min_time


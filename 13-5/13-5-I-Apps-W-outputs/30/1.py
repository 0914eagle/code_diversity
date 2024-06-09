
def solve(n, m, k, x, s, a, b, c, d):
    # Initialize the minimum time to prepare n potions as the initial time
    min_time = x
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
                # If the j-th bit is set, spend the mana cost of the j-th spell
                mana_spent += b[j]
                # If the j-th spell is of the first type, update the preparation time
                if j < k:
                    x = a[j]
        # Loop through all possible combinations of the second type of spells
        for i in range(1 << k):
            # Initialize the number of manapoints spent as 0
            mana_spent += sum(d[j] for j in range(k) if i & (1 << j))
            # Initialize the number of potions prepared as 0
            potions_prepared += sum(c[j] for j in range(k) if i & (1 << j))
            # If the total number of manapoints spent is less than or equal to s, update the minimum time
            if mana_spent <= s:
                min_time = min(min_time, x * (n - potions_prepared) + mana_spent)
    # Return the minimum time to prepare n potions
    return min_time


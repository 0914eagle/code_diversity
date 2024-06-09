
def solve(n, m, k, x, s, a, b, c, d):
    # Initialize the minimum time to prepare n potions as infinity
    min_time = float('inf')
    # Loop through all possible combinations of spells
    for i in range(1 << m):
        # Initialize the current time to prepare n potions as 0
        curr_time = 0
        # Initialize the current number of mana points spent as 0
        mana_spent = 0
        # Loop through all m spells
        for j in range(m):
            # Check if the j-th spell is used in the current combination
            if i & (1 << j):
                # Add the time required to prepare one potion with the j-th spell to the current time
                curr_time += a[j]
                # Add the mana cost of the j-th spell to the total mana spent
                mana_spent += b[j]
        # Loop through all k spells
        for j in range(k):
            # Check if the j-th spell is used in the current combination
            if i & (1 << (m + j)):
                # Add the time required to prepare c[j] potions with the j-th spell to the current time
                curr_time += c[j] * a[j]
                # Add the mana cost of the j-th spell to the total mana spent
                mana_spent += d[j]
        # Check if the current combination of spells allows Anton to prepare at least n potions and uses no more than s mana points
        if curr_time >= n * x and mana_spent <= s:
            # Update the minimum time to prepare n potions if the current time is less than the minimum time
            min_time = min(min_time, curr_time)
    # Return the minimum time to prepare n potions
    return min_time


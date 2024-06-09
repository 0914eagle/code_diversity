
def solve(n, m, k, x, s, a, b, c, d):
    # Initialize the minimum time to prepare n potions as the initial preparation time
    min_time = x
    # Loop through all possible combinations of spells
    for i in range(1 << m):
        # Initialize the number of potions prepared and the number of mana points used
        num_potions, mana_points = 0, 0
        # Loop through all spells
        for j in range(m):
            # Check if the j-th spell is used in the current combination
            if i & (1 << j):
                # Add the number of potions created by the j-th spell to the total number of potions prepared
                num_potions += c[j]
                # Add the cost of the j-th spell to the total number of mana points used
                mana_points += d[j]
        # Check if the total number of mana points used is less than or equal to the maximum allowed
        if mana_points <= s:
            # Loop through all possible combinations of the first type of spell
            for j in range(1 << m):
                # Initialize the number of potions prepared and the preparation time
                num_potions_2, time = 0, 0
                # Loop through all spells of the first type
                for l in range(m):
                    # Check if the l-th spell of the first type is used in the current combination
                    if j & (1 << l):
                        # Add the number of potions created by the l-th spell to the total number of potions prepared
                        num_potions_2 += c[l]
                        # Add the cost of the l-th spell to the total number of mana points used
                        mana_points += d[l]
                        # Add the time required to prepare each potion to the total preparation time
                        time += a[l]
                # Check if the total number of mana points used is less than or equal to the maximum allowed
                if mana_points <= s:
                    # Add the number of potions prepared by the second type of spell to the total number of potions prepared
                    num_potions += num_potions_2
                    # Add the preparation time required by the second type of spell to the total preparation time
                    time += num_potions_2 * a[m]
                    # Update the minimum time to prepare n potions if the current combination is the optimal one
                    min_time = min(min_time, time)
    # Return the minimum time to prepare n potions
    return min_time


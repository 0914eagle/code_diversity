
def get_min_money_to_feed_cat(awakening_time, hunger_level, hunger_increase_per_minute, bun_cost, bun_decrease_hunger):
    # Calculate the total hunger level after awakening
    total_hunger_level = hunger_level + (awakening_time.hour * 60 + awakening_time.minute) * hunger_increase_per_minute

    # Calculate the number of buns needed to feed the cat
    num_buns_needed = total_hunger_level // bun_decrease_hunger

    # Calculate the total cost of buns needed
    total_cost = num_buns_needed * bun_cost

    # Apply discount for buns purchased after 20:00
    if awakening_time.hour >= 20:
        total_cost *= 0.8

    return total_cost


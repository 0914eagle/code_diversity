
def get_minimum_amount_spent(awakening_time, hunger_level, hunger_increase_per_minute, bun_cost, bun_decrease_per_bun):
    # Calculate the total hunger increase over the day
    total_hunger_increase = hunger_increase_per_minute * 60 * 24
    
    # Calculate the number of buns needed to feed the cat
    num_buns_needed = hunger_level // bun_decrease_per_bun
    
    # Calculate the cost of the buns at the discounted rate
    discounted_bun_cost = bun_cost * 0.8
    total_cost = num_buns_needed * discounted_bun_cost
    
    return total_cost


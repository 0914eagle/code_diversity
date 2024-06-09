
def get_min_amount_to_feed_cat(awakening_time, hunger_level, hunger_increase_per_minute, bun_cost, bun_decrease_hunger):
    # Calculate the total hunger increase over the day
    total_hunger_increase = hunger_increase_per_minute * 60 * 24
    
    # Calculate the number of buns needed to feed the cat
    num_buns_needed = hunger_level // bun_decrease_hunger
    
    # Calculate the cost of the buns
    cost_of_buns = num_buns_needed * bun_cost
    
    # Calculate the cost of the buns with the discount
    cost_of_buns_with_discount = cost_of_buns * 0.8
    
    # Calculate the minimum amount needed to feed the cat
    min_amount_needed = cost_of_buns_with_discount
    
    return min_amount_needed


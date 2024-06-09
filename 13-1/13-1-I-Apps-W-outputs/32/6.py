
def get_min_amount_to_feed_cat(awakening_time, hunger_level, hunger_increase_per_minute, bun_cost, bun_decrease_hunger, discount_percentage=20):
    # Calculate the total minutes since awakening
    total_minutes = (awakening_time[0] * 60) + awakening_time[1]
    
    # Calculate the total hunger increase since awakening
    total_hunger_increase = hunger_increase_per_minute * total_minutes
    
    # Calculate the initial hunger level
    initial_hunger_level = hunger_level - total_hunger_increase
    
    # Calculate the number of buns needed to feed the cat
    num_buns_needed = (initial_hunger_level // bun_decrease_hunger) + 1
    
    # Calculate the total cost of buns needed
    total_cost = num_buns_needed * bun_cost
    
    # Apply discount if applicable
    if awakening_time[0] >= 20:
        total_cost = total_cost - (total_cost * (discount_percentage / 100))
    
    return total_cost


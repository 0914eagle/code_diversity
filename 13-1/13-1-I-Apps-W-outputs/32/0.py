
def get_min_money_to_feed_cat(awakening_time, hunger_level, hunger_increase_per_minute, bun_cost, bun_decrease_hunger):
    # Calculate the total minutes until 20:00
    total_minutes = (20 - awakening_time[0]) * 60 + (60 - awakening_time[1])
    
    # Calculate the total hunger increase for the day
    total_hunger_increase = total_minutes * hunger_increase_per_minute
    
    # Calculate the minimum amount of buns needed to feed the cat
    min_buns_needed = hunger_level // bun_decrease_hunger
    
    # Calculate the total cost of buns needed
    total_bun_cost = min_buns_needed * bun_cost
    
    # Calculate the discount for buns purchased after 20:00
    discount = total_bun_cost * 0.2
    
    # Calculate the final cost of buns needed
    final_bun_cost = total_bun_cost - discount
    
    return final_bun_cost


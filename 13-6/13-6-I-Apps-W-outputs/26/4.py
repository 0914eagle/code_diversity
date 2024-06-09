
def get_max_vegetables(m, v, di_list, ai_list):
    # Sort the di_list and ai_list based on the day when the vegetables become edible
    sorted_di_list = sorted(di_list)
    sorted_ai_list = sorted(ai_list, key=lambda x: x[1], reverse=True)
    
    # Initialize variables to keep track of the number of vegetables collected and the current day
    total_vegetables = 0
    current_day = 1
    
    # Loop through the list of vegetables and collect them on the appropriate days
    for di, ai in zip(sorted_di_list, sorted_ai_list):
        # If the current day is within the range of days when the vegetables are edible, collect them
        if current_day >= di and current_day < di+1:
            total_vegetables += ai
            current_day += 1
        # If the current day is beyond the range of days when the vegetables are edible, move on to the next day
        else:
            current_day += 1
    
    # Return the total number of vegetables collected
    return total_vegetables


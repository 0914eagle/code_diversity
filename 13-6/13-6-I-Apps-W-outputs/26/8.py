
def get_max_vegetables(M, V, Di, Ai):
    # Sort the lanes based on the day they become edible
    lanes = sorted(zip(Di, Ai), key=lambda x: x[0])
    
    # Initialize variables to keep track of the number of vegetables collected and the current day
    total_vegetables = 0
    current_day = 1
    
    # Loop through each lane and collect vegetables if they are edible on the current day
    for lane in lanes:
        if lane[0] <= current_day:
            total_vegetables += min(lane[1], V - (total_vegetables % V))
            current_day += 1
    
    return total_vegetables


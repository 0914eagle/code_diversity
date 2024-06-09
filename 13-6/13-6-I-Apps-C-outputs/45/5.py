
def get_total_time(k, d, t):
    # Calculate the time the chicken takes to cook on the turned on stove
    time_on = t
    
    # Calculate the time the chicken takes to cook on the turned off stove
    time_off = 2 * t
    
    # Calculate the total time Julia needs to turn on the stove every d minutes
    total_time_on = k * (time_on / d)
    
    # Calculate the total time Julia needs to turn off the stove every d minutes
    total_time_off = (k - 1) * (time_off / d)
    
    # Calculate the total time Julia needs to turn on and off the stove
    total_time = total_time_on + total_time_off
    
    return total_time


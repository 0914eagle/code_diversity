
def can_prepare_contest(h, m, s, t_1, t_2):
    # Convert the time to a single number of seconds
    time_1 = h * 3600 + m * 60 + s
    time_2 = t_1 * 3600 + t_2 * 60
    
    # Check if the difference between the two times is a multiple of 3600
    if (time_2 - time_1) % 3600 == 0:
        return "YES"
    else:
        return "NO"


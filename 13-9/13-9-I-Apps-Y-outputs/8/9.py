
def get_dog_attacks(aggressive_1, calm_1, aggressive_2, calm_2, arrival_time):
    # Calculate the number of minutes since the start of the day
    current_minute = arrival_time % 1440

    # Calculate the number of minutes until the next aggressive period
    aggressive_1_minutes_left = aggressive_1 - (current_minute % (aggressive_1 + calm_1))
    aggressive_2_minutes_left = aggressive_2 - (current_minute % (aggressive_2 + calm_2))

    # Check if either dog is aggressive during the arrival time
    if aggressive_1_minutes_left == 0 or aggressive_2_minutes_left == 0:
        return "both"
    elif aggressive_1_minutes_left != 0 and aggressive_2_minutes_left != 0:
        return "none"
    else:
        return "one"


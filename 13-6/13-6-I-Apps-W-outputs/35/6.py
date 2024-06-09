
def solve(h1, h2, a, b):
    # Calculate the total distance the caterpillar needs to travel
    total_distance = h2 - h1

    # Calculate the distance the caterpillar travels during the day
    day_distance = a * 10

    # Calculate the distance the caterpillar travels during the night
    night_distance = b * 10

    # Calculate the total number of days it takes for the caterpillar to travel the total distance
    total_days = total_distance // day_distance

    # Check if the caterpillar can reach the apple on the last day
    if total_distance % day_distance == 0:
        return total_days

    # Calculate the number of days the caterpillar spends climbing up and down
    climb_days = total_distance // night_distance

    # Calculate the number of days the caterpillar spends climbing up
    up_days = total_days - climb_days

    # Check if the caterpillar can reach the apple on the last day
    if up_days * day_distance + (total_distance % night_distance) >= h2:
        return total_days

    # If the caterpillar can't reach the apple, return -1
    return -1


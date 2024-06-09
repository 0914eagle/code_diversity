
def solve(h1, h2, a, b):
    # Calculate the total distance the caterpillar needs to travel
    total_distance = h2 - h1

    # Calculate the distance the caterpillar travels during the day
    day_distance = a * 10

    # Calculate the distance the caterpillar travels during the night
    night_distance = b * 10

    # Calculate the number of days it takes for the caterpillar to travel the total distance
    days = total_distance // day_distance

    # Check if the caterpillar can get the apple on the last day
    if total_distance % day_distance == 0:
        return days

    # Check if the caterpillar can get the apple on the first day
    if h1 <= day_distance:
        return 1

    # Check if the caterpillar can get the apple on the last day after slipping down under the ground
    if h2 - h1 <= night_distance:
        return days + 1

    # If the caterpillar can't get the apple, return -1
    return -1


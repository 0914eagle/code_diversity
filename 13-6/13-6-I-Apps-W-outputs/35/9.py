
def solve(h1, h2, a, b):
    # Calculate the total distance the caterpillar needs to travel
    total_distance = h2 - h1

    # Calculate the distance the caterpillar travels during the day
    day_distance = a * 10

    # Calculate the distance the caterpillar travels during the night
    night_distance = b * 10

    # Calculate the total number of days it takes for the caterpillar to travel the total distance
    total_days = total_distance // day_distance

    # Check if the caterpillar can get the apple on the last day
    if total_distance % day_distance == 0:
        return total_days

    # Calculate the number of days the caterpillar spends climbing up during the day
    day_climbing_days = total_distance // day_distance

    # Calculate the number of days the caterpillar spends slipping down during the night
    night_climbing_days = (total_distance - (day_climbing_days * day_distance)) // night_distance

    # Return the total number of days it takes for the caterpillar to get the apple
    return day_climbing_days + night_climbing_days + 1


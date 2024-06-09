
def solve(h1, h2, a, b):
    # Calculate the total distance the caterpillar needs to travel
    total_distance = h2 - h1

    # Calculate the distance the caterpillar travels by day and night
    day_distance = a * 10
    night_distance = b * 10

    # Calculate the number of days it takes for the caterpillar to travel the total distance
    days = total_distance // (day_distance + night_distance)

    # If the caterpillar can't get the apple in the given time frame, return -1
    if days == 0:
        return -1

    # Return the number of days it takes for the caterpillar to get the apple
    return days


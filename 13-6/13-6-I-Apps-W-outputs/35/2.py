
def solve(h1, h2, a, b):
    # Calculate the total distance the caterpillar needs to travel
    total_distance = h2 - h1

    # Calculate the distance the caterpillar travels during the day
    day_distance = a * 10

    # Calculate the distance the caterpillar travels during the night
    night_distance = b * 10

    # Calculate the number of days it takes for the caterpillar to travel the total distance
    days = total_distance // day_distance

    # Calculate the number of hours the caterpillar spends traveling during the night
    night_hours = total_distance % day_distance

    # Calculate the number of days it takes for the caterpillar to travel the night distance
    night_days = night_hours // night_distance

    # Return the total number of days it takes for the caterpillar to get the apple
    return days + night_days


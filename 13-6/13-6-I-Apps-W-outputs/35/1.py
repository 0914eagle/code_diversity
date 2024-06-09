
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

    # Calculate the number of days the caterpillar spends climbing up the tree
    climb_days = h1 // a

    # Calculate the number of days the caterpillar spends slipping down the tree
    slide_days = (h2 - h1) // b

    # Calculate the total number of days the caterpillar spends in the forest
    total_forest_days = climb_days + slide_days + total_days

    # Return the number of days Gabriel needs to wait to see the caterpillar get the apple
    return total_forest_days


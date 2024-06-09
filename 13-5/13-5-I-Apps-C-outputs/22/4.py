
def solve(n, m, e, roads, exits, start_brothers, start_police):
    # Initialize the minimum speed required to escape as infinity
    min_speed = float('inf')

    # Loop through all possible routes the brothers can take
    for route in permutations(range(1, n + 1)):
        # Initialize the current speed of the brothers' car as 0
        curr_speed = 0

        # Loop through each road in the route
        for i in range(m):
            # Get the current intersection and the next intersection
            curr_intersection = route[i]
            next_intersection = route[i + 1]

            # Get the length of the current road
            length = roads[i][2]

            # Calculate the time it takes to travel the current road at the current speed
            time = length / curr_speed

            # Calculate the distance the brothers' car will travel while the police car is traveling the current road
            dist_brothers = curr_speed * time

            # Calculate the distance the police car will travel while the brothers' car is traveling the current road
            dist_police = roads[i][2] / roads[i][1]

            # If the brothers' car will reach the next intersection before the police car, then the brothers can continue on their route
            if dist_brothers <= dist_police:
                # Update the current speed of the brothers' car
                curr_speed = max(curr_speed, roads[i][1])
            else:
                # If the brothers' car will not reach the next intersection before the police car, then the brothers will be caught
                break

        # If the brothers were able to reach the end of their route, then calculate the minimum speed required to escape
        if i == m - 1:
            # Calculate the time it takes for the brothers' car to reach the highway exit
            time = length / curr_speed

            # Calculate the distance the brothers' car will travel while the police car is traveling the current road
            dist_brothers = curr_speed * time

            # Calculate the distance the police car will travel while the brothers' car is traveling the current road
            dist_police = roads[i][2] / roads[i][1]

            # If the brothers' car will reach the highway exit before the police car, then calculate the minimum speed required to escape
            if dist_brothers <= dist_police:
                min_speed = min(min_speed, curr_speed)

    # If the minimum speed is infinity, then it is impossible to escape
    if min_speed == float('inf'):
        return "IMPOSSIBLE"
    else:
        return min_speed


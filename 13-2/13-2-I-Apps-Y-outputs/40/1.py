
def get_min_flight_time(p, q, r):
    # Calculate the sum of the flight times for each route
    route_1 = p + q
    route_2 = q + r
    route_3 = r + p

    # Return the minimum of the three routes
    return min(route_1, route_2, route_3)


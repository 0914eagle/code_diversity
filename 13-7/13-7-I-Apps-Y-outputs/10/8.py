
def get_min_flight_time(p, q, r):
    # Calculate the sum of the flight times for each route
    route_a_to_b_to_c = p + q
    route_a_to_c_to_b = p + r
    route_b_to_a_to_c = q + p
    route_b_to_c_to_a = q + r
    route_c_to_a_to_b = r + p
    route_c_to_b_to_a = r + q

    # Return the minimum of the flight times
    return min(route_a_to_b_to_c, route_a_to_c_to_b, route_b_to_a_to_c, route_b_to_c_to_a, route_c_to_a_to_b, route_c_to_b_to_a)

def main():
    # Read the input from stdin
    p, q, r = map(int, input().split())

    # Call the get_min_flight_time function and print the result
    print(get_min_flight_time(p, q, r))

if __name__ == '__main__':
    main()


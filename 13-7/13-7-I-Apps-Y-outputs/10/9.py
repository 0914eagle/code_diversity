
def get_min_flight_time(p, q, r):
    # Calculate the sum of the flight times for each route
    route_a_b_c = p + q
    route_a_c_b = p + r
    route_b_a_c = q + p
    route_b_c_a = q + r
    route_c_a_b = r + p
    route_c_b_a = r + q

    # Return the minimum of the sum of the flight times
    return min(route_a_b_c, route_a_c_b, route_b_a_c, route_b_c_a, route_c_a_b, route_c_b_a)

def main():
    p, q, r = map(int, input().split())
    print(get_min_flight_time(p, q, r))

if __name__ == '__main__':
    main()


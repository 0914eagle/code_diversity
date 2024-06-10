
def get_flight_times(p, q, r):
    # Calculate the flight times for each route
    routes = [
        (p, q),
        (q, r),
        (r, p),
        (p, r),
        (q, p),
        (r, q)
    ]
    
    # Return the minimum flight time
    return min(sum(route) for route in routes)

def main():
    # Read the input
    p, q, r = map(int, input().split())
    
    # Calculate the minimum flight time
    flight_time = get_flight_times(p, q, r)
    
    # Print the result
    print(flight_time)

if __name__ == '__main__':
    main()


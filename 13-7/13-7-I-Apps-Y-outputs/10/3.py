
def get_flight_times(p, q, r):
    # Calculate the flight times in all possible routes
    routes = []
    routes.append(p + q)
    routes.append(p + r)
    routes.append(q + r)
    routes.append(q + p)
    routes.append(r + p)
    routes.append(r + q)
    
    # Return the minimum flight time
    return min(routes)

def main():
    # Read the input
    p, q, r = map(int, input().split())
    
    # Calculate the minimum flight time
    flight_time = get_flight_times(p, q, r)
    
    # Print the result
    print(flight_time)

if __name__ == '__main__':
    main()


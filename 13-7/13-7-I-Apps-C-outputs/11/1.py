
def get_delivery_time(orders):
    # Initialize variables
    delivery_time = 0
    current_intersection = 1
    current_time = 0

    # Loop through the orders
    for order in orders:
        # Calculate the time it takes to travel from the current intersection to the next intersection
        travel_time = get_travel_time(current_intersection, order[1])

        # Update the current time and intersection
        current_time += travel_time
        current_intersection = order[1]

        # Calculate the delivery time for the current order
        delivery_time += order[2] - current_time

        # Update the current time
        current_time = order[2]

    return delivery_time

def get_travel_time(start_intersection, end_intersection):
    # Initialize variables
    travel_time = 0

    # Loop through the roads
    for road in roads:
        # Check if the road connects the start and end intersections
        if (road[0] == start_intersection and road[1] == end_intersection) or (road[0] == end_intersection and road[1] == start_intersection):
            # Return the travel time for the road
            return road[2]

    # If no road is found, return 0
    return 0

def main():
    # Read the input
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        u, v, d = map(int, input().split())
        roads.append([u, v, d])
    k = int(input())
    orders = []
    for _ in range(k):
        s, u, t = map(int, input().split())
        orders.append([s, u, t])

    # Calculate the delivery time
    delivery_time = get_delivery_time(orders)

    # Print the result
    print(delivery_time)

if __name__ == '__main__':
    main()


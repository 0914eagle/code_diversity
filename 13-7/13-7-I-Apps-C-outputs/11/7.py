
def get_longest_waiting_time(orders, roads):
    # Initialize the longest waiting time to 0
    longest_waiting_time = 0

    # Iterate through the orders
    for order in orders:
        # Get the time it takes to deliver the order
        delivery_time = get_delivery_time(order, roads)

        # Update the longest waiting time if necessary
        if delivery_time > longest_waiting_time:
            longest_waiting_time = delivery_time

    # Return the longest waiting time
    return longest_waiting_time

def get_delivery_time(order, roads):
    # Get the start and end intersections of the order
    start_intersection = order[1]
    end_intersection = order[2]

    # Initialize the delivery time to 0
    delivery_time = 0

    # Iterate through the roads between the start and end intersections
    for road in roads:
        # Get the start and end intersections of the road
        start_road_intersection = road[0]
        end_road_intersection = road[1]

        # Check if the road connects the start and end intersections
        if start_road_intersection == start_intersection and end_road_intersection == end_intersection:
            # Add the time it takes to cross the road to the delivery time
            delivery_time += road[2]

    # Return the delivery time
    return delivery_time

def main():
    # Read the number of road intersections and roads
    n, m = map(int, input().split())

    # Read the roads
    roads = []
    for _ in range(m):
        u, v, d = map(int, input().split())
        roads.append([u, v, d])

    # Read the number of orders
    k = int(input())

    # Read the orders
    orders = []
    for _ in range(k):
        s, u, t = map(int, input().split())
        orders.append([s, u, t])

    # Get the longest waiting time
    longest_waiting_time = get_longest_waiting_time(orders, roads)

    # Print the longest waiting time
    print(longest_waiting_time)

if __name__ == '__main__':
    main()


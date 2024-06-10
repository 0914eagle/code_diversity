
def get_longest_wait_time(orders, roads):
    # Initialize variables
    longest_wait_time = 0
    current_time = 0
    delivery_schedule = []

    # Sort orders by time of placement
    orders.sort(key=lambda x: x[0])

    # Loop through orders
    for order in orders:
        # Get order information
        order_time, order_location, delivery_time = order

        # Find nearest road intersection
        nearest_road_intersection = find_nearest_road_intersection(order_location, roads)

        # Add delivery time to current time
        current_time += delivery_time

        # Add delivery time to schedule
        delivery_schedule.append((current_time, order_location))

        # Update longest wait time
        longest_wait_time = max(longest_wait_time, current_time - order_time)

    return longest_wait_time

def find_nearest_road_intersection(location, roads):
    # Initialize variables
    nearest_road_intersection = None
    min_distance = float('inf')

    # Loop through roads
    for road in roads:
        # Get road information
        road_start, road_end, road_distance = road

        # Find distance from location to road
        distance = abs(location - road_start)

        # Update nearest road intersection and min distance
        if distance < min_distance:
            nearest_road_intersection = road_end
            min_distance = distance

    return nearest_road_intersection

def main():
    # Read input
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        u, v, d = map(int, input().split())
        roads.append((u, v, d))
    k = int(input())
    orders = []
    for _ in range(k):
        s, u, t = map(int, input().split())
        orders.append((s, u, t))

    # Get longest wait time
    longest_wait_time = get_longest_wait_time(orders, roads)

    # Print output
    print(longest_wait_time)

if __name__ == '__main__':
    main()



def get_longest_wait_time(orders, roads, pizzeria_location):
    # Initialize a dictionary to store the shortest distance from the pizzeria to each road intersection
    distances = {}
    for road in roads:
        distances[road[0]] = 0
        distances[road[1]] = 0
    
    # Initialize a priority queue to store the orders
    pq = []
    for order in orders:
        heapq.heappush(pq, (order[1], order[0]))
    
    # Initialize a dictionary to store the delivery time for each order
    delivery_times = {}
    
    # Loop through the orders and calculate the delivery time for each order
    while pq:
        current_time, current_order = heapq.heappop(pq)
        current_location = current_order[0]
        if current_location != pizzeria_location:
            # Calculate the distance from the pizzeria to the current location
            distance = distances[current_location]
            # Calculate the delivery time for the current order
            delivery_time = current_time + distance
            # Update the delivery time for the current order
            delivery_times[current_order] = delivery_time
            # Update the distances for the roads leading to the current location
            for road in roads:
                if road[0] == current_location or road[1] == current_location:
                    distances[road[0]] = min(distances[road[0]], delivery_time + road[2])
                    distances[road[1]] = min(distances[road[1]], delivery_time + road[2])
    
    # Find the longest delivery time
    longest_delivery_time = max(delivery_times.values())
    
    return longest_delivery_time

def main():
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
    print(get_longest_wait_time(orders, roads, 1))

if __name__ == '__main__':
    main()


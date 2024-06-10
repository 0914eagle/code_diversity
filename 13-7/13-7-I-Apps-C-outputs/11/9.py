
def get_longest_wait_time(orders, roads, pizzeria):
    # Initialize a dictionary to store the distance from the pizzeria to each road intersection
    distances = {}
    for road in roads:
        distances[road[0]] = 0
        distances[road[1]] = road[2]
    
    # Initialize a list to store the order times and the corresponding waiting times
    order_times = []
    
    # Loop through the orders and calculate the waiting time for each order
    for order in orders:
        # Get the distance from the pizzeria to the road intersection where the order was placed
        distance = distances[order[1]]
        
        # Calculate the waiting time as the difference between the order time and the delivery time
        waiting_time = order[2] - order[0] - distance
        
        # Add the order time and waiting time to the list
        order_times.append((order[0], waiting_time))
    
    # Sort the list by the waiting time in descending order
    order_times.sort(key=lambda x: x[1], reverse=True)
    
    # Return the longest waiting time
    return order_times[0][1]

def main():
    # Read the number of road intersections and roads
    n, m = map(int, input().split())
    
    # Read the roads
    roads = []
    for _ in range(m):
        u, v, d = map(int, input().split())
        roads.append((u, v, d))
    
    # Read the number of orders
    k = int(input())
    
    # Read the orders
    orders = []
    for _ in range(k):
        s, u, t = map(int, input().split())
        orders.append((s, u, t))
    
    # Call the function to get the longest waiting time
    longest_wait_time = get_longest_wait_time(orders, roads, 1)
    
    # Print the result
    print(longest_wait_time)

if __name__ == '__main__':
    main()


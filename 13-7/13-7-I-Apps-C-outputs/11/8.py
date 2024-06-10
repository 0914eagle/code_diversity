
def read_input():
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
    return n, m, roads, k, orders

def optimize_delivery(n, m, roads, k, orders):
    # Initialize the delivery schedule with the order times
    delivery_schedule = [order[1] for order in orders]

    # Sort the orders by the time they were placed
    orders.sort(key=lambda x: x[0])

    # Iterate through the orders and update the delivery schedule
    for order in orders:
        # Find the earliest road intersection that can be reached from the current intersection
        earliest_intersection = -1
        for road in roads:
            if road[0] == order[1] and road[1] not in delivery_schedule:
                earliest_intersection = road[1]
                break

        # If an earlier intersection is found, update the delivery schedule
        if earliest_intersection != -1:
            delivery_schedule.append(earliest_intersection)

    # Return the longest time a customer has to wait
    return max(orders[i][2] - orders[i-1][2] for i in range(1, len(orders)))

def main():
    n, m, roads, k, orders = read_input()
    print(optimize_delivery(n, m, roads, k, orders))

if __name__ == '__main__':
    main()


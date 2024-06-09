
def get_longest_waiting_time(n, m, roads, orders):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for u, v, d in roads:
        graph[u - 1].append((v - 1, d))
        graph[v - 1].append((u - 1, d))

    # Sort the orders by time of placement
    orders.sort(key=lambda x: x[0])

    # Initialize the delivery schedule with the first order
    schedule = [orders[0]]

    # Iterate through the remaining orders
    for order in orders[1:]:
        # Find the earliest time that the pizza can be delivered
        earliest_time = order[0]
        for prev_order in schedule:
            earliest_time = max(earliest_time, prev_order[1] + graph[prev_order[2] - 1][order[2] - 1][1])

        # If the earliest time is after the current time, add the order to the schedule
        if earliest_time >= order[1]:
            schedule.append(order)

    # Return the longest waiting time
    return max(order[1] - order[0] for order in schedule)

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
    print(get_longest_waiting_time(n, m, roads, orders))

if __name__ == '__main__':
    main()


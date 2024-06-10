
def get_longest_wait_time(orders, roads, pizzeria_location):
    # Initialize a dictionary to store the distance from the pizzeria to each intersection
    distances = {}
    for intersection in roads:
        distances[intersection] = float('inf')
    distances[pizzeria_location] = 0

    # Use Breadth-First Search to find the shortest distance from the pizzeria to each intersection
    queue = [pizzeria_location]
    while queue:
        current_intersection = queue.pop(0)
        for neighbor in roads[current_intersection]:
            if distances[neighbor] == float('inf'):
                distances[neighbor] = distances[current_intersection] + 1
                queue.append(neighbor)

    # Use the shortest distance from the pizzeria to each intersection to determine the longest wait time for each order
    longest_wait_time = 0
    for order in orders:
        wait_time = distances[order[1]] + order[2] - order[0]
        longest_wait_time = max(longest_wait_time, wait_time)

    return longest_wait_time

def main():
    n, m = map(int, input().split())
    roads = {}
    for _ in range(m):
        u, v, d = map(int, input().split())
        roads[u] = roads.get(u, []) + [v]
        roads[v] = roads.get(v, []) + [u]
    k = int(input())
    orders = []
    for _ in range(k):
        s, u, t = map(int, input().split())
        orders.append((s, u, t))
    pizzeria_location = 1
    print(get_longest_wait_time(orders, roads, pizzeria_location))

if __name__ == '__main__':
    main()


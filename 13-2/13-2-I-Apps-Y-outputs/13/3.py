
def get_least_time(intersections, streets, start_intersection, end_intersection, k):
    # Initialize a dictionary to store the time it takes to reach each intersection
    times = {start_intersection: 0}
    queue = [start_intersection]

    # Breadth-first search to calculate the time it takes to reach each intersection
    while queue:
        intersection = queue.pop(0)
        for street in streets:
            if street[0] == intersection:
                neighbor = street[1]
                time = times[intersection] + street[2]
                if neighbor not in times or time < times[neighbor]:
                    times[neighbor] = time
                    queue.append(neighbor)

    # Calculate the least time it takes to make the delivery
    return times[end_intersection] + k

def main():
    intersections, streets, start_intersection, end_intersection, k = map(int, input().split())
    streets = [tuple(map(int, input().split())) for _ in range(streets)]
    print(get_least_time(intersections, streets, start_intersection, end_intersection, k))

if __name__ == '__main__':
    main()


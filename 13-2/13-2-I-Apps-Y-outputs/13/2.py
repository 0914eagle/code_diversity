
def get_least_time(intersections, streets, start_intersection, end_intersection, k):
    # Initialize a dictionary to store the time it takes to reach each intersection
    time_dict = {start_intersection: 0}
    queue = [start_intersection]

    while queue:
        current_intersection = queue.pop(0)
        for street in streets:
            if street[0] == current_intersection:
                next_intersection = street[1]
                time_dict[next_intersection] = time_dict[current_intersection] + street[2]
                queue.append(next_intersection)

    # Calculate the least time it takes to reach the end intersection
    least_time = float('inf')
    for intersection in time_dict:
        if intersection == end_intersection:
            least_time = min(least_time, time_dict[intersection])
        elif intersection in intersections:
            least_time = min(least_time, time_dict[intersection] + k)

    return least_time

def main():
    intersections, streets, start_intersection, end_intersection, k = map(int, input().split())
    intersections = set(map(int, input().split()))
    streets = []
    for _ in range(streets):
        streets.append(list(map(int, input().split())))
    print(get_least_time(intersections, streets, start_intersection, end_intersection, k))

if __name__ == '__main__':
    main()


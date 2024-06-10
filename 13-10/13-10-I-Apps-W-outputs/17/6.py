
def get_min_distance(rooms, k):
    # Find the indices of the k available rooms
    available_rooms = [i for i, room in enumerate(rooms) if room == "0"]
    # Initialize the minimum distance to a large value
    min_distance = float("inf")
    # Iterate over all possible combinations of k available rooms
    for combination in itertools.combinations(available_rooms, k + 1):
        # Calculate the distance between the first room and the last room in the combination
        distance = abs(combination[-1] - combination[0])
        # Update the minimum distance if necessary
        min_distance = min(min_distance, distance)
    return min_distance

def main():
    n, k = map(int, input().split())
    rooms = input()
    print(get_min_distance(rooms, k))

if __name__ == '__main__':
    main()


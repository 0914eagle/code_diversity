
def get_max_distance(rooms, k):
    # Find the index of the first unoccupied room
    first_unoccupied = next((i for i, room in enumerate(rooms) if room == "0"), None)
    # Find the index of the last unoccupied room
    last_unoccupied = next(
        (i for i in range(len(rooms) - 1, -1, -1) if rooms[i] == "0"), None
    )
    # Calculate the maximum distance between the first unoccupied room and the last unoccupied room
    max_distance = abs(last_unoccupied - first_unoccupied)
    # If there are more than k + 1 unoccupied rooms, we can choose any subset of k + 1 unoccupied rooms and calculate the maximum distance
    if len(rooms) - sum(rooms) > k + 1:
        for i in range(first_unoccupied, last_unoccupied + 1):
            for j in range(i + 1, last_unoccupied + 1):
                distance = abs(j - i)
                if distance > max_distance:
                    max_distance = distance
    return max_distance

def main():
    n, k = map(int, input().split())
    rooms = list(input())
    print(get_max_distance(rooms, k))

if __name__ == "__main__":
    main()


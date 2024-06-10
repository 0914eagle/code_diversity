
def find_k_distant_rooms(rooms, k):
    # Find the indices of the k closest unoccupied rooms to Farmer John's room
    closest_rooms = []
    for i in range(len(rooms)):
        if rooms[i] == "0":
            closest_rooms.append(i)
            if len(closest_rooms) == k:
                break

    # Find the maximum distance between Farmer John's room and any of the k closest unoccupied rooms
    max_distance = 0
    for i in range(len(closest_rooms)):
        for j in range(i+1, len(closest_rooms)):
            distance = abs(closest_rooms[i] - closest_rooms[j])
            if distance > max_distance:
                max_distance = distance

    return max_distance

def main():
    n, k = map(int, input().split())
    rooms = list(input())
    print(find_k_distant_rooms(rooms, k))

if __name__ == '__main__':
    main()


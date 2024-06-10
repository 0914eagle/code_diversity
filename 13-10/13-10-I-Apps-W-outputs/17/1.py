
def find_min_distance(rooms, k):
    # Find the indices of the k+1 unoccupied rooms
    unoccupied_rooms = [i for i, room in enumerate(rooms) if room == "0"]
    occupied_rooms = [i for i, room in enumerate(rooms) if room == "1"]
    k_plus_1_rooms = unoccupied_rooms[:k+1]

    # Calculate the distance between Farmer John's room and the furthest cow's room
    furthest_room = k_plus_1_rooms[-1]
    min_distance = abs(furthest_room - k_plus_1_rooms[0])

    return min_distance

def main():
    n, k = map(int, input().split())
    rooms = input()
    min_distance = find_min_distance(rooms, k)
    print(min_distance)

if __name__ == '__main__':
    main()



def get_unoccupied_rooms(n, k, occupied_rooms):
    unoccupied_rooms = []
    for i in range(n):
        if occupied_rooms[i] == "0":
            unoccupied_rooms.append(i)
    return unoccupied_rooms

def get_min_distance(unoccupied_rooms, k):
    min_distance = float("inf")
    for i in range(len(unoccupied_rooms)):
        for j in range(i+1, min(i+k+1, len(unoccupied_rooms))):
            distance = abs(unoccupied_rooms[j] - unoccupied_rooms[i])
            if distance < min_distance:
                min_distance = distance
    return min_distance

def solve(n, k, occupied_rooms):
    unoccupied_rooms = get_unoccupied_rooms(n, k, occupied_rooms)
    min_distance = get_min_distance(unoccupied_rooms, k)
    return min_distance

if __name__ == '__main__':
    n, k = map(int, input().split())
    occupied_rooms = input()
    print(solve(n, k, occupied_rooms))



import sys

def get_input():
    N, M = map(int, input().split())
    rooms = set(range(N))
    doors = set()
    for _ in range(M):
        u, v = map(int, input().split())
        if u != v:
            doors.add((u, v))
    return N, M, rooms, doors

def find_optimal_door(N, M, rooms, doors):
    # Initialize a dictionary to store the number of rooms that can be reached from each room
    reachable_rooms = {room: set() for room in rooms}
    for door in doors:
        reachable_rooms[door[0]].add(door[1])
        reachable_rooms[door[1]].add(door[0])
    
    # Initialize a set to store the rooms that can be reached from the outside
    outside_rooms = set()
    for door in doors:
        if door[0] == -1 or door[1] == -1:
            outside_rooms.add(door[0])
            outside_rooms.add(door[1])
    
    # Find the door that leads to the maximum number of rooms that can only be reached from the outside
    max_rooms = 0
    optimal_door = None
    for door in doors:
        if door[0] == -1 or door[1] == -1:
            continue
        reachable_rooms_from_door = reachable_rooms[door[0]] | reachable_rooms[door[1]]
        num_rooms = len(reachable_rooms_from_door & outside_rooms)
        if num_rooms > max_rooms:
            max_rooms = num_rooms
            optimal_door = door
    
    return optimal_door

def main():
    N, M, rooms, doors = get_input()
    optimal_door = find_optimal_door(N, M, rooms, doors)
    print(optimal_door)

if __name__ == '__main__':
    main()


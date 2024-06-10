
def get_cycle_count(rooms, corridors):
    # Initialize a dictionary to store the number of corridors from each room
    room_corridors = {room: 0 for room in rooms}
    
    # Iterate over the corridors and increment the number of corridors from each room
    for corridor in corridors:
        room_corridors[corridor[0]] += 1
        room_corridors[corridor[1]] += 1
    
    # Initialize a set to store the rooms with an odd number of corridors
    odd_rooms = set()
    
    # Iterate over the rooms and check if the number of corridors is odd
    for room, corridor_count in room_corridors.items():
        if corridor_count % 2 == 1:
            odd_rooms.add(room)
    
    # Return the number of corridors to be removed
    return len(odd_rooms)

def remove_corridors(rooms, corridors, max_corridors_to_remove):
    # Initialize a set to store the rooms with an odd number of corridors
    odd_rooms = set()
    
    # Iterate over the corridors and check if the number of corridors is odd
    for corridor in corridors:
        room_a, room_b = corridor
        if room_a in odd_rooms or room_b in odd_rooms:
            continue
        room_corridors = {room: 0 for room in rooms}
        room_corridors[room_a] += 1
        room_corridors[room_b] += 1
        for room, corridor_count in room_corridors.items():
            if corridor_count % 2 == 1:
                odd_rooms.add(room)
    
    # Initialize a list to store the corridors to be removed
    corridors_to_remove = []
    
    # Iterate over the corridors and check if they should be removed
    for corridor in corridors:
        room_a, room_b = corridor
        if room_a in odd_rooms or room_b in odd_rooms:
            corridors_to_remove.append(corridor)
    
    # Return the list of corridors to be removed
    return corridors_to_remove[:max_corridors_to_remove]

def main():
    # Read the input
    rooms, corridors = map(int, input().split())
    corridors = [tuple(map(int, input().split())) for _ in range(corridors)]
    
    # Get the number of corridors to be removed
    corridors_to_remove = get_cycle_count(rooms, corridors)
    
    # Remove the corridors
    corridors_to_remove = remove_corridors(rooms, corridors, corridors_to_remove)
    
    # Print the output
    print(len(corridors_to_remove))
    for corridor in corridors_to_remove:
        print(*corridor)

if __name__ == '__main__':
    main()


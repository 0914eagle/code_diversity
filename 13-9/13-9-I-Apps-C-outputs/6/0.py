
def solve(r, l, rooms):
    # Initialize a list to store the hit rooms
    hit_rooms = []
    
    # Iterate over the rooms
    for room in rooms:
        # Calculate the area of the current room
        area = (room[2] - room[0]) * (room[3] - room[1])
        
        # Check if the room is hit by the phaser beam
        if area > 0:
            # Add the room to the list of hit rooms
            hit_rooms.append(room)
    
    # Return the number of hit rooms
    return len(hit_rooms)


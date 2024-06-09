
def get_room_assignment(events):
    # Initialize the room assignment list with all rooms as empty
    room_assignment = [0] * 10
    
    # Iterate through the events
    for event in events:
        # If the event is 'L', a customer has arrived from the left entrance
        if event == 'L':
            # Find the first empty room from the left entrance
            empty_room = room_assignment.index(0)
            # Assign the customer to that room
            room_assignment[empty_room] = 1
        # If the event is 'R', a customer has arrived from the right entrance
        elif event == 'R':
            # Find the first empty room from the right entrance
            empty_room = room_assignment.index(0, 5)
            # Assign the customer to that room
            room_assignment[empty_room] = 1
        # If the event is a digit (i.e., a customer has left a room)
        elif event.isdigit():
            # Get the room number from the event
            room_number = int(event)
            # Release the room
            room_assignment[room_number] = 0
    
    # Return the final room assignment list
    return room_assignment

def main():
    # Get the number of events from the user
    n = int(input())
    # Get the events from the user
    events = input()
    
    # Call the get_room_assignment function to get the room assignment list
    room_assignment = get_room_assignment(events)
    
    # Print the final room assignment list
    print("".join(str(room) for room in room_assignment))

if __name__ == '__main__':
    main()



def get_room_assignment(events):
    # Initialize the room assignment list with all rooms empty
    room_assignment = [0] * 10
    
    # Iterate through the events
    for event in events:
        # If the event is 'L', a customer arrives from the left entrance
        if event == 'L':
            # Find the first empty room from the left entrance
            for i in range(10):
                if room_assignment[i] == 0:
                    room_assignment[i] = 1
                    break
        # If the event is 'R', a customer arrives from the right entrance
        elif event == 'R':
            # Find the first empty room from the right entrance
            for i in range(10):
                if room_assignment[9 - i] == 0:
                    room_assignment[9 - i] = 1
                    break
        # If the event is a digit (0-9), a customer in that room leaves
        elif event.isdigit():
            # Set the room to empty
            room_assignment[int(event)] = 0
    
    # Return the final room assignment list
    return room_assignment

def main():
    # Read the number of events and the events from stdin
    n = int(input())
    events = input()
    
    # Call the get_room_assignment function and print the result
    print("".join(str(room) for room in get_room_assignment(events)))

if __name__ == '__main__':
    main()



def get_room_assignment(events):
    # Initialize an empty list to store the room assignment
    room_assignment = [0] * 10
    
    # Iterate through the events
    for event in events:
        # If the event is 'L', assign the customer to the first empty room from the left
        if event == 'L':
            for i in range(10):
                if room_assignment[i] == 0:
                    room_assignment[i] = 1
                    break
        # If the event is 'R', assign the customer to the first empty room from the right
        elif event == 'R':
            for i in range(9, -1, -1):
                if room_assignment[i] == 0:
                    room_assignment[i] = 1
                    break
        # If the event is a digit (0-9), mark the corresponding room as empty
        else:
            room_assignment[int(event)] = 0
    
    # Return the final room assignment
    return ''.join(str(room) for room in room_assignment)

def main():
    # Read the number of events and the events from stdin
    n = int(input())
    events = input()
    
    # Get the room assignment from the events
    room_assignment = get_room_assignment(events)
    
    # Print the room assignment
    print(room_assignment)

if __name__ == '__main__':
    main()



def get_room_assignment(events):
    # Initialize an empty list to store the room assignment
    room_assignment = []
    
    # Iterate through the events
    for event in events:
        # If the event is 'L', append a 1 to the list
        if event == 'L':
            room_assignment.append(1)
        # If the event is 'R', append a 0 to the list
        elif event == 'R':
            room_assignment.append(0)
        # If the event is a digit, remove the corresponding digit from the list
        else:
            room_assignment.remove(int(event))
    
    # Return the final room assignment list
    return room_assignment

def main():
    # Read the number of events and the events from the input
    n = int(input())
    events = input()
    
    # Call the get_room_assignment function and print the result
    print("".join(map(str, get_room_assignment(events))))

if __name__ == '__main__':
    main()


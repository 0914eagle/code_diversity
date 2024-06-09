
def get_room_assignment_list(events):
    # Initialize the room assignment list with all zeros
    room_assignment_list = [0] * 10
    
    # Iterate through the events
    for event in events:
        # If the event is 'L', assign the next available room to the customer from the left entrance
        if event == 'L':
            room_assignment_list[room_assignment_list.index(0)] = 1
        # If the event is 'R', assign the next available room to the customer from the right entrance
        elif event == 'R':
            room_assignment_list[9 - room_assignment_list[::-1].index(0)] = 1
        # If the event is a digit (i.e., a room number), mark the corresponding room as empty
        else:
            room_assignment_list[int(event)] = 0
    
    return "".join(str(x) for x in room_assignment_list)

def main():
    # Read the number of events and the events from stdin
    n = int(input())
    events = input()
    
    # Get the room assignment list
    room_assignment_list = get_room_assignment_list(events)
    
    # Print the room assignment list
    print(room_assignment_list)

if __name__ == '__main__':
    main()


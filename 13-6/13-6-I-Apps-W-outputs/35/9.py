
def get_room_assignment_list(events):
    # Initialize the room assignment list with all zeros
    room_assignment_list = [0] * 10
    
    # Iterate through the events
    for event in events:
        # If the event is 'L', assign the next empty room to the customer from the left entrance
        if event == 'L':
            # Find the first empty room from the left entrance
            empty_room_index = room_assignment_list.index(0)
            # Assign the room to the customer
            room_assignment_list[empty_room_index] = 1
        # If the event is 'R', assign the next empty room to the customer from the right entrance
        elif event == 'R':
            # Find the first empty room from the right entrance
            empty_room_index = room_assignment_list.index(0, 5)
            # Assign the room to the customer
            room_assignment_list[empty_room_index] = 1
        # If the event is a number between 0 and 9, mark the corresponding room as empty
        elif event.isdigit() and int(event) < 10:
            room_assignment_list[int(event)] = 0
    
    return "".join(str(room) for room in room_assignment_list)

def main():
    # Read the number of events
    num_events = int(input())
    # Read the events
    events = input()
    
    # Get the room assignment list
    room_assignment_list = get_room_assignment_list(events)
    
    # Print the room assignment list
    print(room_assignment_list)

if __name__ == '__main__':
    main()


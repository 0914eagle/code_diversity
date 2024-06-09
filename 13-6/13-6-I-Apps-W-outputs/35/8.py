
def get_room_assignment_list(events):
    # Initialize an empty list to store the room assignment
    room_assignment = [0] * 10
    # Iterate through the events
    for event in events:
        # If the event is 'L', assign the next empty room to the customer from the left entrance
        if event == 'L':
            room_assignment[room_assignment.index(0)] = 1
        # If the event is 'R', assign the next empty room to the customer from the right entrance
        elif event == 'R':
            room_assignment[9 - room_assignment[::-1].index(0)] = 1
        # If the event is a digit (i.e., a customer leaving a room), mark the corresponding room as empty
        else:
            room_assignment[int(event)] = 0
    return ''.join(str(x) for x in room_assignment)

def main():
    n = int(input())
    events = input()
    print(get_room_assignment_list(events))

if __name__ == '__main__':
    main()


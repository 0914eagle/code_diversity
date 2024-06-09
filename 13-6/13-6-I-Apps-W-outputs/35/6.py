
def get_room_assignment(n, events):
    # Initialize an empty array to store the room assignment
    room_assignment = [0] * 10
    
    # Iterate through the events
    for event in events:
        # If the event is 'L', assign the next empty room to the customer from the left entrance
        if event == 'L':
            room_assignment[room_assignment.index(0)] = 1
        # If the event is 'R', assign the next empty room to the customer from the right entrance
        elif event == 'R':
            room_assignment[9 - room_assignment[::-1].index(0)] = 1
        # If the event is a digit, mark the corresponding room as empty
        else:
            room_assignment[int(event)] = 0
    
    # Return the final room assignment
    return ''.join(str(x) for x in room_assignment)

def main():
    n = int(input())
    events = input()
    print(get_room_assignment(n, events))

if __name__ == '__main__':
    main()


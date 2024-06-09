
def get_elevator_sequence(floors, start, goal, up, down):
    # Initialize variables
    current_floor = start
    sequence = []
    pushes = 0

    # Loop until the goal floor is reached or the elevator cannot reach it
    while current_floor != goal and current_floor >= 0 and current_floor <= floors:
        # Check if the goal floor is above the current floor
        if goal > current_floor:
            # Check if the elevator can reach the goal floor with the "up" button
            if current_floor + up <= goal:
                # Add the "up" button to the sequence and update the current floor
                sequence.append("up")
                current_floor += up
                pushes += 1
            else:
                # The elevator cannot reach the goal floor with the "up" button, so use the "down" button
                sequence.append("down")
                current_floor -= down
                pushes += 1
        else:
            # The goal floor is below the current floor
            if current_floor - down >= goal:
                # Add the "down" button to the sequence and update the current floor
                sequence.append("down")
                current_floor -= down
                pushes += 1
            else:
                # The elevator cannot reach the goal floor with the "down" button, so use the "up" button
                sequence.append("up")
                current_floor += up
                pushes += 1

    # If the goal floor is reached, return the sequence of button presses
    if current_floor == goal:
        return sequence, pushes
    else:
        # If the elevator cannot reach the goal floor, return the message "use the stairs"
        return "use the stairs", 0

def main():
    # Read the input
    floors, start, goal, up, down = map(int, input().split())

    # Get the elevator sequence and the number of pushes
    sequence, pushes = get_elevator_sequence(floors, start, goal, up, down)

    # Print the output
    print(sequence)
    print(pushes)

if __name__ == '__main__':
    main()


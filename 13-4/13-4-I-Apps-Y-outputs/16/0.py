
def get_elevator_sequence(floors, start, goal, up, down):
    # Initialize variables
    current_floor = start
    sequence = []
    pushes = 0

    # Loop until the goal floor is reached or the elevator cannot reach the goal floor
    while current_floor != goal and current_floor >= 0 and current_floor <= floors:
        # Check if the goal floor is above the current floor
        if goal > current_floor:
            # Check if the elevator can reach the goal floor with the "up" button
            if current_floor + up <= floors:
                # Add the "up" button to the sequence
                sequence.append("up")
                # Increment the current floor
                current_floor += up
                # Increment the number of pushes
                pushes += 1
            else:
                # The elevator cannot reach the goal floor with the "up" button, so use the "down" button
                if current_floor - down >= 0:
                    # Add the "down" button to the sequence
                    sequence.append("down")
                    # Decrement the current floor
                    current_floor -= down
                    # Increment the number of pushes
                    pushes += 1
                else:
                    # The elevator cannot reach the goal floor with the "down" button, so use the stairs
                    return "use the stairs"
        # Check if the goal floor is below the current floor
        else:
            # Check if the elevator can reach the goal floor with the "down" button
            if current_floor - down >= 0:
                # Add the "down" button to the sequence
                sequence.append("down")
                # Decrement the current floor
                current_floor -= down
                # Increment the number of pushes
                pushes += 1
            else:
                # The elevator cannot reach the goal floor with the "down" button, so use the "up" button
                if current_floor + up <= floors:
                    # Add the "up" button to the sequence
                    sequence.append("up")
                    # Increment the current floor
                    current_floor += up
                    # Increment the number of pushes
                    pushes += 1
                else:
                    # The elevator cannot reach the goal floor with the "up" button, so use the stairs
                    return "use the stairs"

    # Return the sequence of button presses
    return sequence

def main():
    # Read the input
    floors, start, goal, up, down = map(int, input().split())

    # Get the elevator sequence
    sequence = get_elevator_sequence(floors, start, goal, up, down)

    # Print the sequence
    print(sequence)

if __name__ == '__main__':
    main()


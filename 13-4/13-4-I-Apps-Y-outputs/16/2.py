
def get_shortest_sequence(floors, start, goal, up, down):
    # Initialize the shortest sequence as 0
    shortest_sequence = 0
    
    # Loop through each floor from start to goal
    for floor in range(start, goal + 1):
        # If the floor is within the range of the elevator's up button
        if floor <= up:
            # Increment the shortest sequence by 1
            shortest_sequence += 1
        # If the floor is within the range of the elevator's down button
        elif floor >= down:
            # Increment the shortest sequence by 1
            shortest_sequence += 1
        # If the floor is not within the range of either button
        else:
            # Break the loop and return "use the stairs"
            return "use the stairs"
    
    # Return the shortest sequence
    return shortest_sequence

def main():
    # Read the input from stdin
    floors, start, goal, up, down = map(int, input().split())
    
    # Call the get_shortest_sequence function and print the result
    print(get_shortest_sequence(floors, start, goal, up, down))

if __name__ == '__main__':
    main()


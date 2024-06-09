
def get_shortest_sequence(floors, start, goal, up, down):
    # Initialize the shortest sequence as 0
    shortest_sequence = 0
    
    # Loop through each floor from start to goal
    for floor in range(start, goal + 1):
        # If the floor is not reachable, return "use the stairs"
        if floor > floors:
            return "use the stairs"
        
        # If the floor is reachable, increment the shortest sequence
        shortest_sequence += 1
    
    # Return the shortest sequence
    return shortest_sequence

def main():
    # Read the input from stdin
    floors, start, goal, up, down = map(int, input().split())
    
    # Call the get_shortest_sequence function and print the result
    print(get_shortest_sequence(floors, start, goal, up, down))

if __name__ == '__main__':
    main()


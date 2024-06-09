
def get_elevator_sequence(floors, start, goal, up, down):
    # Initialize variables
    current_floor = start
    sequence = []
    pushes = 0

    # Loop until the goal floor is reached or the elevator cannot reach the goal floor
    while current_floor != goal and current_floor <= floors:
        # Check if the elevator can reach the goal floor by pressing the UP button
        if current_floor + up <= floors and current_floor + up >= goal:
            sequence.append("UP")
            current_floor += up
            pushes += 1
        # Check if the elevator can reach the goal floor by pressing the DOWN button
        elif current_floor - down >= 1 and current_floor - down <= floors and current_floor - down >= goal:
            sequence.append("DOWN")
            current_floor -= down
            pushes += 1
        # If the elevator cannot reach the goal floor, return "use the stairs"
        else:
            return "use the stairs"

    # Return the sequence of button presses
    return sequence, pushes

def main():
    floors = int(input())
    start = int(input())
    goal = int(input())
    up = int(input())
    down = int(input())
    sequence, pushes = get_elevator_sequence(floors, start, goal, up, down)
    print(sequence)
    print(pushes)

if __name__ == '__main__':
    main()


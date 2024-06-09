
def f1(R, C, maze):
    # Initialize variables
    joe_location = []
    fire_location = []
    exit_location = []
    time = 0
    possible_exit = False

    # Find Joe's location, fire location, and exit location
    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'J':
                joe_location = [i, j]
            elif maze[i][j] == 'F':
                fire_location.append([i, j])
            elif maze[i][j] == '.':
                exit_location.append([i, j])

    # Check if Joe can escape the maze
    while time <= R*C:
        # Move Joe one step
        new_joe_location = [joe_location[0] + 1, joe_location[1]]
        if new_joe_location[0] == R:
            new_joe_location[0] = 0
        if new_joe_location in exit_location:
            possible_exit = True
            break
        joe_location = new_joe_location

        # Move the fire one step
        for i in range(len(fire_location)):
            new_fire_location = [fire_location[i][0] + 1, fire_location[i][1]]
            if new_fire_location[0] == R:
                new_fire_location[0] = 0
            fire_location[i] = new_fire_location

        # Check if the fire has reached Joe's location
        if joe_location in fire_location:
            possible_exit = False
            break

        time += 1

    # Return the output
    if possible_exit:
        return time
    else:
        return "IMPOSSIBLE"

def f2(R, C, maze):
    # Initialize variables
    joe_location = []
    fire_location = []
    exit_location = []
    time = 0
    possible_exit = False

    # Find Joe's location, fire location, and exit location
    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'J':
                joe_location = [i, j]
            elif maze[i][j] == 'F':
                fire_location.append([i, j])
            elif maze[i][j] == '.':
                exit_location.append([i, j])

    # Check if Joe can escape the maze
    while time <= R*C:
        # Move Joe one step
        new_joe_location = [joe_location[0], joe_location[1] + 1]
        if new_joe_location[1] == C:
            new_joe_location[1] = 0
        if new_joe_location in exit_location:
            possible_exit = True
            break
        joe_location = new_joe_location

        # Move the fire one step
        for i in range(len(fire_location)):
            new_fire_location = [fire_location[i][0], fire_location[i][1] + 1]
            if new_fire_location[1] == C:
                new_fire_location[1] = 0
            fire_location[i] = new_fire_location

        # Check if the fire has reached Joe's location
        if joe_location in fire_location:
            possible_exit = False
            break

        time += 1

    # Return the output
    if possible_exit:
        return time
    else:
        return "IMPOSSIBLE"

if __name__ == '__main__':
    R, C = map(int, input().split())
    maze = [input() for i in range(R)]
    print(f1(R, C, maze))
    print(f2(R, C, maze))



def solve(n):
    # Initialize variables
    commands = []
    boxes = []
    reorder_count = 0

    # Iterate through the input
    for i in range(2*n):
        # Get the current command
        command = input().split()

        # Add the command to the list of commands
        commands.append(command)

        # If the command is to add a box, add it to the list of boxes
        if command[0] == "add":
            boxes.append(int(command[1]))

    # Sort the list of boxes in ascending order
    boxes.sort()

    # Iterate through the commands
    for i in range(len(commands)):
        # If the command is to remove a box, check if the box is on top of the stack
        if commands[i][0] == "remove":
            # If the box is not on top of the stack, reorder the stack and increment the reorder count
            if boxes[-1] != int(commands[i][1]):
                reorder_count += 1

    # Return the minimum number of times Daru needs to reorder the boxes
    return reorder_count


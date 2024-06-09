
def solve(n, commands):
    # Initialize variables
    boxes = []
    reorder_count = 0

    # Iterate through the commands
    for command in commands:
        # Add command
        if command.startswith("add"):
            boxes.append(int(command.split()[1]))
        # Remove command
        elif command.startswith("remove"):
            # Check if the box to be removed is at the top of the stack
            if boxes[-1] == n:
                # Remove the box from the stack
                boxes.pop()
            # The box to be removed is not at the top of the stack, so reorder the boxes
            else:
                reorder_count += 1
                # Reorder the boxes by moving the box to be removed to the top of the stack
                boxes.insert(0, boxes.pop())

    # Return the minimum number of times Daru needs to reorder the boxes
    return reorder_count


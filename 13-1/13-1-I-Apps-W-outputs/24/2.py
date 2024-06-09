
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
            else:
                # Reorder the boxes
                reorder_count += 1
                boxes = sorted(boxes)

    return reorder_count


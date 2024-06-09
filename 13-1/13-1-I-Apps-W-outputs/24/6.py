
def solve(n, commands):
    # Initialize variables
    boxes = []
    reorder_count = 0

    # Iterate through the commands
    for command in commands:
        # Add command
        if command.startswith("add"):
            box_id = int(command.split()[1])
            boxes.append(box_id)
        # Remove command
        elif command.startswith("remove"):
            # Check if the box is on the top of the stack
            if boxes and boxes[-1] == n:
                # Remove the box from the stack
                boxes.pop()
            else:
                # Reorder the boxes
                reorder_count += 1
                boxes = sorted(boxes)

    return reorder_count


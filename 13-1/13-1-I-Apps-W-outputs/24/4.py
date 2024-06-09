
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
            # Check if the top box is the required box
            if boxes and boxes[-1] == n:
                boxes.pop()
            # Reorder the boxes if the top box is not the required box
            else:
                reorder_count += 1
                boxes = sorted(boxes)

    # Return the minimum number of times Daru needs to reorder the boxes
    return reorder_count


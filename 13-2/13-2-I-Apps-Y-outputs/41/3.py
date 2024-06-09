
def safe_order(n, students):
    # Initialize the pile with the first room's exams
    pile = students[0]
    visited = set()
    order = []

    # Loop through the rooms
    for i in range(1, n):
        # If the pile is empty, return "impossible"
        if pile == 0:
            return "impossible"

        # Add the current room to the visited set
        visited.add(i)

        # Distribute the exams from the pile to the current room
        pile -= min(pile, students[i] - 1)

        # Add the current room to the order
        order.append(i)

        # If the current room has only one student, continue to the next room
        if students[i] == 1:
            continue

        # If the pile is empty, return "impossible"
        if pile == 0:
            return "impossible"

        # Distribute the exams from the pile to the next room
        pile -= min(pile, students[i + 1] - 1)

        # Add the next room to the order
        order.append(i + 1)

    # If the pile is not empty, return "impossible"
    if pile > 0:
        return "impossible"

    # Return the safe order
    return order


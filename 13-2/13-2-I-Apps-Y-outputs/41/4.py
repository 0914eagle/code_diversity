
def safe_order(n, students):
    # Initialize the pile with the first room's exams
    pile = students[0]
    visited = set()
    order = []

    # Iterate through the rooms in a random order
    for i in range(n):
        # If the current room has not been visited yet, visit it
        if i not in visited:
            # Add the current room's exams to the pile
            pile += students[i]
            # Remove the current room from the visited set
            visited.remove(i)
            # Add the current room to the order
            order.append(i)

            # If the pile contains more exams than the number of students in the next room,
            # visit the next room and remove its exams from the pile
            if len(visited) > 0 and pile > students[min(visited)]:
                next_room = min(visited)
                pile -= students[next_room]
                visited.remove(next_room)
                order.append(next_room)

    # If the pile is empty, return the order, otherwise return "impossible"
    return "impossible" if pile > 0 else order


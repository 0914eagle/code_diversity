
def is_possible(configuration_senior, configuration_student):
    # Initialize a set to store the rooms visited by the senior student
    visited_rooms_senior = set()
    # Initialize a set to store the rooms visited by the student
    visited_rooms_student = set()
    # Initialize a queue to store the rooms to visit
    queue = [1]
    # Loop until the queue is empty
    while queue:
        # Dequeue a room from the queue
        current_room = queue.pop(0)
        # If the room is blocked, continue to the next room
        if configuration_senior[current_room - 1][0] == 0:
            continue
        # If the room is the dormitory, return True
        if current_room == len(configuration_senior):
            return True
        # Add the current room to the set of visited rooms
        visited_rooms_senior.add(current_room)
        # Add the rooms leading to the current room to the queue
        for i in range(1, 5):
            if configuration_senior[current_room - 1][i - 1] != 0:
                queue.append(configuration_senior[current_room - 1][i - 1])
    # Loop until the queue is empty
    while queue:
        # Dequeue a room from the queue
        current_room = queue.pop(0)
        # If the room is blocked, continue to the next room
        if configuration_student[current_room - 1][0] == 0:
            continue
        # If the room is the dormitory, return True
        if current_room == len(configuration_student):
            return True
        # Add the current room to the set of visited rooms
        visited_rooms_student.add(current_room)
        # Add the rooms leading to the current room to the queue
        for i in range(1, 5):
            if configuration_student[current_room - 1][i - 1] != 0:
                queue.append(configuration_student[current_room - 1][i - 1])
    # If the sets of visited rooms are equal, return True
    if visited_rooms_senior == visited_rooms_student:
        return True
    # Otherwise, return False
    return False


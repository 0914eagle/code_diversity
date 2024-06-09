
def restore_queue(n, students):
    # Initialize a dictionary to map each student ID to its index in the queue
    student_index = {student[0]: i for i, student in enumerate(students)}
    
    # Initialize a list to store the final order of the queue
    queue = [0] * n
    
    # Iterate over the students and their neighbors
    for student in students:
        # If the student has a neighbor in front of them
        if student[0] != 0:
            # Get the index of the neighbor in the queue
            neighbor_index = student_index[student[0]]
            # Insert the student after the neighbor in the queue
            queue.insert(neighbor_index + 1, student[1])
        # If the student has a neighbor behind them
        if student[1] != 0:
            # Get the index of the neighbor in the queue
            neighbor_index = student_index[student[1]]
            # Insert the student before the neighbor in the queue
            queue.insert(neighbor_index, student[0])
    
    # Return the final order of the queue
    return queue


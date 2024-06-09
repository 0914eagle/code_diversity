
def restore_queue(students):
    # Initialize a dictionary to map student IDs to their indices in the queue
    student_indices = {student_id: i for i, student_id in enumerate(students)}
    
    # Initialize a list to store the final order of the students
    ordered_students = [0] * len(students)
    
    # Iterate through the students and their neighbors
    for student_id, neighbor_ids in students:
        # If the student has a neighbor in front of them, add them to the list
        if neighbor_ids[0] != 0:
            ordered_students[student_indices[neighbor_ids[0]]] = student_id
        # If the student has a neighbor behind them, add them to the list
        if neighbor_ids[1] != 0:
            ordered_students[student_indices[neighbor_ids[1]] - 1] = student_id
    
    # Return the final order of the students
    return ordered_students


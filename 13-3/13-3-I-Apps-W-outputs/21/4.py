
def restore_queue(n, students):
    # Initialize a dictionary to map each student ID to its index in the queue
    student_indices = {student[0]: i for i, student in enumerate(students)}
    
    # Initialize a list to store the final order of the queue
    queue = [0] * n
    
    # Iterate over the students and their neighbors
    for student in students:
        # Get the index of the student in the queue
        index = student_indices[student[0]]
        
        # If the student has a neighbor in front of them, add them to the queue
        if student[1] != 0:
            queue[index] = student[1]
        
        # If the student has a neighbor behind them, add them to the queue
        if student[2] != 0:
            queue[index + 1] = student[2]
    
    # Return the final order of the queue
    return queue


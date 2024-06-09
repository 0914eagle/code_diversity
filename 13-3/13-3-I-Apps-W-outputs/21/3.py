
def restore_queue(students):
    # Initialize a dictionary to map each student ID to its index in the queue
    student_indices = {student[0]: i for i, student in enumerate(students)}
    
    # Initialize a list to store the final order of the queue
    queue = [0] * len(students)
    
    # Iterate over the students and their neighbors
    for student in students:
        # If the student has a neighbor in front of them, insert them into the queue after their neighbor
        if student[1] != 0:
            queue[student_indices[student[1]] + 1] = student[0]
        # If the student has a neighbor behind them, insert them into the queue before their neighbor
        if student[2] != 0:
            queue[student_indices[student[2]]] = student[0]
    
    return queue


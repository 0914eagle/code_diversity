
def restore_queue(students):
    # Initialize a dictionary to map student IDs to their indices in the queue
    student_indices = {}
    for i, student in enumerate(students):
        student_indices[student] = i
    
    # Initialize a list to store the final order of the queue
    queue = [0] * len(students)
    
    # Iterate through the students and their neighbors
    for student, ahead, behind in students:
        # If the student has a neighbor ahead of them, insert them into the queue after the neighbor
        if ahead != 0:
            queue[student_indices[ahead] + 1] = student
        # If the student has a neighbor behind them, insert them into the queue before the neighbor
        if behind != 0:
            queue[student_indices[behind]] = student
    
    # Return the final order of the queue
    return queue


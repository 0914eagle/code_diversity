
def restore_queue(students):
    # Initialize a dictionary to map each student ID to its index in the queue
    student_indices = {student_id: i for i, student_id in enumerate(students)}
    
    # Initialize a list to store the final order of the queue
    queue = [0] * len(students)
    
    # Iterate over the students and their neighbors
    for i, (front, back) in enumerate(students):
        # If the student has a neighbor in front of them, add them to the queue
        if front != 0:
            queue[student_indices[front]] = students[i]
        
        # If the student has a neighbor behind them, add them to the queue
        if back != 0:
            queue[student_indices[back]] = students[i]
    
    # Return the final order of the queue
    return queue


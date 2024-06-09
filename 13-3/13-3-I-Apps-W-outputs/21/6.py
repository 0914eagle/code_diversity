
def restore_queue(records):
    # Initialize a dictionary to map each student ID to its neighbor IDs
    neighbors = {}
    for record in records:
        front, back = record
        if front != 0:
            neighbors[back] = front
        if back != 0:
            neighbors[front] = back
    
    # Initialize a list to store the sequence of student IDs
    queue = []
    
    # Start from the student at the front of the queue
    current = neighbors[0]
    while current != 0:
        queue.append(current)
        current = neighbors[current]
    
    return queue


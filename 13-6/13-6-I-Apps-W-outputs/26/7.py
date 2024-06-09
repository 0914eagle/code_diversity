
def get_neighbors(students):
    # Initialize a dictionary to store the neighbors
    neighbors = {}
    
    # Iterate over the students and their neighbors
    for student, neighbor in students:
        # If the student has a neighbor, add them to the dictionary
        if neighbor != 0:
            neighbors[student] = neighbor
    
    # Return the dictionary of neighbors
    return neighbors

def restore_queue(neighbors):
    # Initialize an empty list to store the queue
    queue = []
    
    # Get the first student in the queue
    current_student = min(neighbors, key=neighbors.get)
    
    # Loop until the queue is complete
    while len(queue) < len(neighbors):
        # Add the current student to the queue
        queue.append(current_student)
        
        # Get the next student in the queue
        current_student = neighbors[current_student]
    
    # Return the queue
    return queue

def main():
    # Read the number of students
    n = int(input())
    
    # Read the students and their neighbors
    students = []
    for _ in range(n):
        student, neighbor = map(int, input().split())
        students.append((student, neighbor))
    
    # Get the neighbors of each student
    neighbors = get_neighbors(students)
    
    # Restore the queue
    queue = restore_queue(neighbors)
    
    # Print the queue
    print(*queue)

if __name__ == '__main__':
    main()



def get_neighbors(n, students):
    # Initialize an empty dictionary to store the neighbors
    neighbors = {}
    
    # Iterate over the list of students
    for i, student in enumerate(students):
        # Get the ID of the student and the IDs of their neighbors
        id, front, back = student
        
        # If the student has a neighbor in front of them, add them to the dictionary
        if front != 0:
            neighbors[id] = (front, back)
    
    # Return the dictionary of neighbors
    return neighbors

def restore_queue(n, students):
    # Get the neighbors of each student
    neighbors = get_neighbors(n, students)
    
    # Initialize an empty list to store the sequence of IDs
    queue = []
    
    # Start at the student with ID 1 and iterate until the end of the queue is reached
    current = 1
    while current != 0:
        # Add the current student to the queue
        queue.append(current)
        
        # Get the ID of the student's neighbor in front of them
        front = neighbors[current][0]
        
        # Set the current student to their neighbor in front of them
        current = front
    
    # Return the sequence of IDs
    return queue

def main():
    # Read the number of students and the neighbors of each student
    n = int(input())
    students = []
    for i in range(n):
        front, back = map(int, input().split())
        students.append((i+1, front, back))
    
    # Restore the queue
    queue = restore_queue(n, students)
    
    # Print the sequence of IDs
    print(*queue)

if __name__ == '__main__':
    main()



def restore_queue(n, a, b):
    # Initialize a dictionary to map each student ID to its index in the queue
    student_ids = {i: i for i in range(1, n + 1)}
    # Initialize a list to store the sequence of student IDs in the correct order
    sequence = []
    # Iterate through the pairs of student IDs and their neighbors
    for i in range(n):
        # If the student has a neighbor in front of them
        if a[i] != 0:
            # Insert the student ID before its neighbor
            student_ids[a[i]] = student_ids[b[i]]
        # If the student has a neighbor behind them
        if b[i] != 0:
            # Insert the student ID after its neighbor
            student_ids[b[i]] = student_ids[a[i]]
    # Iterate through the dictionary and append the student IDs to the sequence in the correct order
    for i in range(1, n + 1):
        sequence.append(student_ids[i])
    return sequence

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    sequence = restore_queue(n, a, b)
    print(*sequence, sep=' ')

if __name__ == '__main__':
    main()


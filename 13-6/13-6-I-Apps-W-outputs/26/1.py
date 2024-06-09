
def read_input():
    n = int(input())
    queue = []
    for i in range(n):
        a, b = map(int, input().split())
        queue.append((a, b))
    return queue

def restore_queue(queue):
    # Initialize the queue with the first student
    x = [queue[0][0]]
    # Iterate through the rest of the students
    for i in range(1, len(queue)):
        # If the student has a neighbor in front of them
        if queue[i][0] != 0:
            # Find the index of the neighbor in the queue
            index = next((j for j, x_j in enumerate(x) if x_j == queue[i][0]), None)
            # Insert the current student after the neighbor
            x.insert(index + 1, queue[i][1])
        # If the student has a neighbor behind them
        if queue[i][1] != 0:
            # Find the index of the neighbor in the queue
            index = next((j for j, x_j in enumerate(x) if x_j == queue[i][1]), None)
            # Insert the current student before the neighbor
            x.insert(index, queue[i][0])
    return x

def print_output(x):
    print(*x)

if __name__ == '__main__':
    queue = read_input()
    x = restore_queue(queue)
    print_output(x)


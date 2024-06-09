
def solve(n):
    # Initialize a set to store the numbers that have already been visited
    visited = set()
    # Initialize a queue to store the numbers to be visited
    queue = [n]
    # Initialize a variable to store the minimum number of moves required to obtain 1
    min_moves = 0
    # Loop until the queue is empty
    while queue:
        # Get the current number from the queue
        num = queue.pop(0)
        # If the current number is 1, return the minimum number of moves required to obtain it
        if num == 1:
            return min_moves
        # If the current number has already been visited, skip it
        if num in visited:
            continue
        # Add the current number to the set of visited numbers
        visited.add(num)
        # If the current number is divisible by 2, add its half to the queue
        if num % 2 == 0:
            queue.append(num // 2)
        # If the current number is divisible by 3, add its double divided by 3 to the queue
        if num % 3 == 0:
            queue.append(num // 3 * 2)
        # If the current number is divisible by 5, add its double divided by 5 to the queue
        if num % 5 == 0:
            queue.append(num // 5 * 4)
        # Increment the minimum number of moves required to obtain 1
        min_moves += 1
    # If the queue is empty and 1 has not been found, return -1
    return -1


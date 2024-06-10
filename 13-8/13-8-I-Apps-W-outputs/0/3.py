
def get_synchronized_stones(c_stones, t_stones):
    # Initialize a queue to store the indices of the stones to be synchronized
    queue = [i for i in range(1, len(c_stones)) if c_stones[i] != t_stones[i]]

    # Loop until the queue is empty
    while queue:
        # Get the index of the stone to be synchronized
        i = queue.pop(0)

        # Synchronize the stone with its neighbors
        c_stones[i] = c_stones[i + 1] + c_stones[i - 1] - c_stones[i]

        # If the synchronized charge is not equal to the target charge, add the stone's index to the queue
        if c_stones[i] != t_stones[i]:
            queue.append(i)

    # Return True if all stones have been synchronized, False otherwise
    return all(c_stones[i] == t_stones[i] for i in range(len(c_stones)))

def main():
    # Read the input
    n = int(input())
    c_stones = list(map(int, input().split()))
    t_stones = list(map(int, input().split()))

    # Check if the stones can be synchronized
    if get_synchronized_stones(c_stones, t_stones):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()


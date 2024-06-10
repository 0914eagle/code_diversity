
def get_min_shuffles(n, s, t, shuffle_ops):
    # Initialize a list to store the current position of the marble
    marble_pos = [s]
    # Initialize a set to store the visited positions
    visited = set()
    # Initialize a variable to store the minimum number of shuffles
    min_shuffles = 0

    # Loop through the shuffle operations
    for i in range(len(shuffle_ops)):
        # Get the current position of the marble
        curr_pos = marble_pos[i]
        # Get the next position of the marble
        next_pos = shuffle_ops[i]
        # Add the current position to the visited set
        visited.add(curr_pos)
        # Move the marble to the next position
        marble_pos[i] = next_pos
        # If the marble has reached the final position, break the loop
        if next_pos == t:
            break
        # If the marble has visited a position before, it means it has looped back to the initial position
        # and it is impossible to get the marble to the final position
        if next_pos in visited:
            return -1
        # Increment the minimum number of shuffles
        min_shuffles += 1

    # If the marble has not reached the final position, it is impossible to get it there
    if marble_pos[-1] != t:
        return -1

    # Return the minimum number of shuffles
    return min_shuffles

def main():
    n, s, t = map(int, input().split())
    shuffle_ops = list(map(int, input().split()))
    print(get_min_shuffles(n, s, t, shuffle_ops))

if __name__ == '__main__':
    main()


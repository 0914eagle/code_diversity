
def get_min_shuffles(n, s, t, shuffles):
    # Initialize a list to store the current position of the marble
    marble_pos = [s]
    # Initialize a set to store the visited positions
    visited = set()
    # Initialize a variable to store the minimum number of shuffles
    min_shuffles = 0

    # Loop through the shuffling operations
    for shuffle in shuffles:
        # Get the current position of the marble
        curr_pos = marble_pos[-1]
        # Get the new position of the marble according to the shuffling operation
        new_pos = shuffle[curr_pos - 1]
        # Add the new position to the list of visited positions
        visited.add(new_pos)
        # Add the new position to the list of marble positions
        marble_pos.append(new_pos)
        # Increment the minimum number of shuffles
        min_shuffles += 1

    # If the marble has reached the final position, return the minimum number of shuffles
    if marble_pos[-1] == t:
        return min_shuffles
    # If the marble has visited all positions and still hasn't reached the final position, return -1
    elif len(visited) == n:
        return -1
    # If the marble has not visited all positions and has not reached the final position, return -1
    else:
        return -1

def main():
    n, s, t = map(int, input().split())
    shuffles = [list(map(int, input().split())) for _ in range(n)]
    print(get_min_shuffles(n, s, t, shuffles))

if __name__ == '__main__':
    main()


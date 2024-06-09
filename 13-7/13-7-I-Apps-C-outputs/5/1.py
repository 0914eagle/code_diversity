
def get_largest_connected_group_of_trees(heights, growth_speeds):
    # Initialize a dictionary to store the tree heights and their connections
    tree_heights = {}
    for i in range(len(heights)):
        for j in range(len(heights[0])):
            tree_heights[(i, j)] = heights[i][j]

    # Initialize a queue to store the trees to be processed
    queue = []

    # Add the first tree to the queue
    queue.append((0, 0))

    # Loop until the queue is empty
    while queue:
        # Get the current tree from the queue
        current_tree = queue.pop(0)

        # Get the current tree height and growth speed
        current_height = tree_heights[current_tree]
        current_growth_speed = growth_speeds[current_tree]

        # Check if the current tree is connected to any other trees
        for neighbor in get_neighbors(current_tree, heights):
            # If the neighboring tree is not connected, add it to the queue
            if neighbor not in tree_heights:
                queue.append(neighbor)
                tree_heights[neighbor] = current_height + current_growth_speed

    # Return the largest connected group of trees
    return max(tree_heights.values())

def get_neighbors(tree, heights):
    # Get the row and column of the current tree
    row, col = tree

    # Initialize a list to store the neighbors
    neighbors = []

    # Check if the tree has any neighbors in the top row
    if row > 0:
        # Add the top neighbor to the list
        neighbors.append((row - 1, col))

    # Check if the tree has any neighbors in the bottom row
    if row < len(heights) - 1:
        # Add the bottom neighbor to the list
        neighbors.append((row + 1, col))

    # Check if the tree has any neighbors in the left column
    if col > 0:
        # Add the left neighbor to the list
        neighbors.append((row, col - 1))

    # Check if the tree has any neighbors in the right column
    if col < len(heights[0]) - 1:
        # Add the right neighbor to the list
        neighbors.append((row, col + 1))

    return neighbors

def main():
    # Read the input from stdin
    heights = []
    for _ in range(int(input())):
        heights.append(list(map(int, input().split())))
    growth_speeds = []
    for _ in range(int(input())):
        growth_speeds.append(list(map(int, input().split())))

    # Call the function to get the largest connected group of trees
    largest_connected_group = get_largest_connected_group_of_trees(heights, growth_speeds)

    # Print the result
    print(largest_connected_group)

if __name__ == "__main__":
    main()


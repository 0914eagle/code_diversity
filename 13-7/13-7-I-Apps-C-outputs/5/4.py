
def get_largest_connected_group(heights, growth_speeds):
    # Initialize a dictionary to store the tree heights and their connections
    tree_dict = {}
    for i in range(len(heights)):
        for j in range(len(heights[0])):
            tree_dict[(i, j)] = (heights[i][j], set())

    # Iterate over the tree dictionary and connect adjacent trees
    for i in range(len(heights)):
        for j in range(len(heights[0])):
            if (i, j) in tree_dict:
                # Get the current tree's height and connections
                curr_height, curr_connections = tree_dict[(i, j)]
                # Check if the tree has already been visited
                if not curr_height:
                    continue
                # Get the neighbors of the current tree
                neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                # Iterate over the neighbors and connect adjacent trees
                for neighbor in neighbors:
                    # Check if the neighbor is out of bounds or has already been visited
                    if not (0 <= neighbor[0] < len(heights) and 0 <= neighbor[1] < len(heights[0])) or neighbor in curr_connections:
                        continue
                    # Get the neighbor's height and connections
                    neighbor_height, neighbor_connections = tree_dict[neighbor]
                    # Check if the neighbor is connected to the current tree
                    if neighbor_height == curr_height:
                        # Add the current tree to the neighbor's connections
                        neighbor_connections.add((i, j))
                        # Add the neighbor to the current tree's connections
                        curr_connections.add(neighbor)
                        # Update the tree dictionary with the new connections
                        tree_dict[neighbor] = (neighbor_height, neighbor_connections)
                        tree_dict[(i, j)] = (curr_height, curr_connections)

    # Find the largest connected group of trees
    largest_group = []
    for tree in tree_dict:
        if tree_dict[tree][0] and tree not in largest_group:
            largest_group.append(tree)
            for connected_tree in tree_dict[tree][1]:
                largest_group.append(connected_tree)

    return len(largest_group)

def main():
    heights = []
    growth_speeds = []
    for _ in range(int(input())):
        heights.append(list(map(int, input().split())))
        growth_speeds.append(list(map(int, input().split())))
    print(get_largest_connected_group(heights, growth_speeds))

if __name__ == "__main__":
    main()


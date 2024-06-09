
def get_min_islands(image):
    # Initialize a 2D array to keep track of the number of islands
    num_islands = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]
    # Initialize a 2D array to keep track of the number of clouds
    num_clouds = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]
    # Initialize a queue to keep track of the cells to be processed
    queue = []
    # Loop through the image and count the number of islands and clouds
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] == "L":
                num_islands[i][j] += 1
            elif image[i][j] == "C":
                num_clouds[i][j] += 1
                queue.append((i, j))
    # Loop through the queue and process each cell
    while queue:
        i, j = queue.pop(0)
        # If the cell is a land cell and it has not been processed yet, mark it as processed and add it to the number of islands
        if image[i][j] == "L" and num_islands[i][j] == 0:
            num_islands[i][j] += 1
            # Add the cell's neighbors to the queue
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < len(image) and 0 <= y < len(image[0]):
                    queue.append((x, y))
    # Return the minimum number of islands
    return min(num_islands[i][j] for i in range(len(image)) for j in range(len(image[0])))


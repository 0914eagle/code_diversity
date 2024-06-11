def minPath(grid, k):
    
    # initialize the queue
    queue = [(0, 0, 0, [])]
    # initialize the visited set
    visited = set()
    # initialize the result
    result = []
    # loop while the queue is not empty
    while queue:
        # pop the first element from the queue
        i, j, step, path = queue.pop(0)
        # if the current step is greater than the given k
        if step > k:
            continue
        # if the current step is equal to the given k
        if step == k:
            # append the current path to the result
            result.append(path)
            continue
        # if the current cell is not visited
        if (i, j) not in visited:
            # mark the current cell as visited
            visited.add((i, j))
            # if the current cell is valid
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                # append the current cell to the current path
                path.append(grid[i][j])
                # push the current cell to the queue
                queue.append((i, j, step + 1, path))
                # push the left neighbor cell to the queue
                queue.append((i, j - 1, step + 1, path))
                # push the right neighbor cell to the queue
                queue.append((i, j + 1, step + 1, path))
                # push the top neighbor cell to the queue
                queue.append((i - 1, j, step + 1, path))
                # push the bottom neighbor cell to the queue
                queue.append((i + 1, j, step + 1, path))
    # return the result
    return result[0]


if __name__ == "__main__":
    print(minPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3))
    print(minPath([[5, 9, 3], [4, 1, 6], [7, 8, 2]], 1))

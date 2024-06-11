def minPath(grid, k):
    
    # initialize the grid
    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        for j in range(m):
            grid[i][j] = (grid[i][j], i, j)

    # initialize the heap
    heap = []
    for i in range(n):
        for j in range(m):
            heapq.heappush(heap, grid[i][j])

    # initialize the visited set
    visited = set()

    # initialize the result
    result = []

    # initialize the k
    k = k - 1

    # start the loop
    while k >= 0:
        # pop the top element from the heap
        top = heapq.heappop(heap)

        # get the top element
        top_val = top[0]

        # get the top i and j
        top_i = top[1]
        top_j = top[2]

        # if the top element is in the visited set
        if top_val in visited:
            # continue the loop
            continue

        # add the top element to the visited set
        visited.add(top_val)

        # add the top element to the result
        result.append(top_val)

        # decrease the k
        k = k - 1

        # if the k is negative
        if k < 0:
            # break the loop
            break

        # if the top i is not 0
        if top_i != 0:
            # add the top i - 1, top j to the heap
            heapq.heappush(heap, grid[top_i - 1][top_j])

        # if the top j is not 0
        if top_j != 0:
            # add the top i, top j - 1 to the heap
            heapq.heappush(heap, grid[top_i][top_j - 1])

        # if the top i is not n - 1
        if top_i != n - 1:
            # add the top i
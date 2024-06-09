
def solve(n, m, a, b, x):
    # Initialize a 2D array to store the dot product of a and b
    c = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            c[i][j] = a[i] * b[j]

    # Initialize a variable to store the maximum area
    max_area = 0

    # Iterate over all possible positions of the top-left corner
    for i in range(n):
        for j in range(m):
            # Initialize variables to store the current area and sum
            area = 0
            sum = 0

            # Iterate over the elements in the current subrectangle
            for k in range(i, n):
                for l in range(j, m):
                    # Add the current element to the sum and increment the area
                    sum += c[k][l]
                    area += 1

                    # If the sum exceeds x, break out of the loop
                    if sum > x:
                        break

                # If the area exceeds the maximum area, update the maximum area and break out of the loop
                if area > max_area:
                    max_area = area
                    break

            # If the area exceeds the maximum area, update the maximum area
            if area > max_area:
                max_area = area

    # Return the maximum area
    return max_area


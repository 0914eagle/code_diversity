
def get_max_deliciousness(x, y, a, b, c, p, q, r):
    # Initialize the maximum possible sum of deliciousness as 0
    max_sum = 0

    # Loop through all possible combinations of eating red and green apples
    for i in range(x + 1):
        for j in range(y + 1):
            # Calculate the sum of deliciousness for the current combination
            sum = 0
            for k in range(i):
                sum += p[k]
            for k in range(j):
                sum += q[k]
            for k in range(c):
                sum += r[k]

            # Update the maximum possible sum if the current combination is better
            if sum > max_sum:
                max_sum = sum

    return max_sum


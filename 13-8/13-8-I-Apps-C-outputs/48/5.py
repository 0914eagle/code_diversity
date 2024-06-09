
def solve(n, distances):
    # Initialize the disparity of each shipment as 0
    disparity = [0] * n

    # Loop through each shipment
    for i in range(n):
        # Loop through each other shipment
        for j in range(i+1, n):
            # Calculate the distance between the two shipments
            distance = distances[i][j]

            # If the distance is greater than the current disparity, update the disparity
            if distance > disparity[i]:
                disparity[i] = distance
            if distance > disparity[j]:
                disparity[j] = distance

    # Partition the shipments into two groups based on their disparities
    group_1 = []
    group_2 = []
    for i in range(n):
        if disparity[i] == 0:
            group_1.append(i)
        else:
            group_2.append(i)

    # Calculate the sum of the disparities for each group
    sum_1 = sum(disparity[i] for i in group_1)
    sum_2 = sum(disparity[i] for i in group_2)

    # Return the minimum possible sum of disparities
    return min(sum_1, sum_2)


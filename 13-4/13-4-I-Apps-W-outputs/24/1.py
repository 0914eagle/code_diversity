
def is_possible_to_choose_three_musketeers(n, m, pairs):
    # Initialize a list to store the recognition of each warrior
    recognitions = [0] * (n + 1)

    # Loop through each pair of warriors knowing each other
    for i in range(m):
        # Get the indices of the two warriors
        a, b = pairs[i]

        # Increment the recognition of both warriors by 1
        recognitions[a] += 1
        recognitions[b] += 1

    # Find the indices of the three musketeers with the minimum recognition sum
    min_sum = float("inf")
    min_indices = []
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                if recognitions[i] + recognitions[j] + recognitions[k] < min_sum:
                    min_sum = recognitions[i] + recognitions[j] + recognitions[k]
                    min_indices = [i, j, k]

    # Check if it is possible to choose three musketeers with the minimum recognition sum
    if min_sum == float("inf"):
        return -1
    else:
        return min_sum


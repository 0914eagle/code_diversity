
def solve(n, m, edges):
    # Initialize a dictionary to store the recognition of each warrior
    recognitions = {i: 0 for i in range(1, n + 1)}

    # Iterate over the edges and update the recognition of each warrior
    for edge in edges:
        recognitions[edge[0]] += 1
        recognitions[edge[1]] += 1

    # Find the three musketeers with the minimum recognition sum
    min_sum = float('inf')
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                if recognitions[i] + recognitions[j] + recognitions[k] < min_sum:
                    min_sum = recognitions[i] + recognitions[j] + recognitions[k]

    # If a triple of musketeers is found, return the minimum recognition sum
    # Otherwise, return -1
    if min_sum < float('inf'):
        return min_sum
    else:
        return -1


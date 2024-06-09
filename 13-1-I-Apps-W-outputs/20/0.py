
def solve(sizes, costs):
    # Sort the sizes in non-decreasing order
    sorted_sizes = sorted(sizes)

    # Initialize the minimum total cost to infinity
    min_cost = float("inf")

    # Iterate over all possible triples of indices
    for i in range(len(sizes) - 2):
        for j in range(i + 1, len(sizes) - 1):
            for k in range(j + 1, len(sizes)):
                # Check if the sizes are in non-decreasing order
                if sorted_sizes[i] < sorted_sizes[j] < sorted_sizes[k]:
                    # Calculate the total cost for this triple
                    total_cost = costs[i] + costs[j] + costs[k]

                    # Update the minimum total cost if necessary
                    if total_cost < min_cost:
                        min_cost = total_cost

    # Return the minimum total cost or -1 if no valid triple exists
    return -1 if min_cost == float("inf") else min_cost


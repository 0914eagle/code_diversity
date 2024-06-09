
def solve(n, results):
    # Sort the results in ascending order
    sorted_results = sorted(results)

    # Initialize the finalists array
    finalists = ["0"] * n

    # Set the k value to 0 for now
    k = 0

    # Loop through the results and find the winners from both semifinals
    for i in range(n):
        if sorted_results[i] in results:
            finalists[i] = "1"

    # Return the finalists array
    return finalists


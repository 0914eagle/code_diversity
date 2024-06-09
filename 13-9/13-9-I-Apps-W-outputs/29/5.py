
def get_chance_to_advance(n, results):
    # Sort the results in ascending order
    sorted_results = sorted(results)

    # Find the k value that maximizes the number of participants advancing to the finals
    k = 0
    while k < n - 1:
        # Calculate the number of participants advancing to the finals with k = k
        num_advance = k + (n - 2*k)

        # If the number of participants advancing to the finals is less than or equal to n, we have found the maximum k value
        if num_advance <= n:
            break

        # Increment k
        k += 1

    # Initialize the output strings
    output1 = ""
    output2 = ""

    # Loop through the results and determine which participants have any chance to advance to the finals
    for i in range(n):
        # If the result is in the top k places in the first or second semifinal, the participant has a chance to advance to the finals
        if sorted_results[i] in results[:k] or sorted_results[i] in results[-k:]:
            output1 += "1"
            output2 += "1"
        else:
            output1 += "0"
            output2 += "0"

    return [output1, output2]


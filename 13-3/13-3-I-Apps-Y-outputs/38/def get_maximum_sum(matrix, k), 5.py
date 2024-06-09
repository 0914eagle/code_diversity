
def get_maximum_sum(matrix, k):
    # Initialize the maximum sum to 0
    max_sum = 0
    # Loop through each row of the matrix
    for row in matrix:
        # Get the number of elements that can be chosen in this row
        num_elements = int(len(row) / 2)
        # Initialize a set to store the chosen elements
        chosen_elements = set()
        # Loop through each element in the row
        for element in row:
            # If the element is not already in the chosen elements set, add it to the set
            if element not in chosen_elements:
                chosen_elements.add(element)
                # If the number of elements in the set is equal to the number of elements that can be chosen, break the loop
                if len(chosen_elements) == num_elements:
                    break
        # Calculate the sum of the chosen elements
        sum_chosen = sum(chosen_elements)
        # If the sum is divisible by k and is greater than the current maximum sum, update the maximum sum
        if sum_chosen % k == 0 and sum_chosen > max_sum:
            max_sum = sum_chosen
    # Return the maximum sum
    return max_sum


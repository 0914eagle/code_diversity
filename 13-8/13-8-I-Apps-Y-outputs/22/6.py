
def get_number_of_solved_problems(n, k, difficulties):
    # Initialize variables
    left_index = 0
    right_index = n - 1
    number_of_solved_problems = 0

    # Iterate through the list of difficulties
    while left_index <= right_index:
        # Check if the difficulty of the leftmost problem is less than or equal to k
        if difficulties[left_index] <= k:
            # Increment the number of solved problems
            number_of_solved_problems += 1
            # Remove the leftmost problem from the list
            difficulties.pop(left_index)
            # Decrement the size of the list
            n -= 1
        # Check if the difficulty of the rightmost problem is less than or equal to k
        elif difficulties[right_index] <= k:
            # Increment the number of solved problems
            number_of_solved_problems += 1
            # Remove the rightmost problem from the list
            difficulties.pop(right_index)
            # Decrement the size of the list
            n -= 1
        # If the difficulty of both problems is greater than k, break the loop
        else:
            break

    # Return the number of solved problems
    return number_of_solved_problems


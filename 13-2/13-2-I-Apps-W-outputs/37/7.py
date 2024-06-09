
def get_max_sum(n, a, b):
    # Initialize the maximum sum to 0
    max_sum = 0
    # Iterate over all possible groups of students
    for i in range(n):
        for j in range(i+1, n):
            # Check if the current group of students can work together calmly
            if can_work_together(a[i], a[j]):
                # Calculate the sum of the skill levels of the current group of students
                current_sum = b[i] + b[j]
                # Update the maximum sum if necessary
                max_sum = max(max_sum, current_sum)
    # Return the maximum sum
    return max_sum

def can_work_together(a, b):
    # Initialize the result to True
    result = True
    # Iterate over all possible algorithms
    for i in range(60):
        # Check if the current algorithm is known by both students
        if (a & (1 << i)) and (b & (1 << i)):
            # If the current algorithm is known by both students, the result is False
            result = False
            break
    # Return the result
    return result


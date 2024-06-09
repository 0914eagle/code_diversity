
def get_max_sum(n, a, b):
    # Initialize the maximum sum to 0
    max_sum = 0
    # Iterate over all possible groups of students
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            # Check if the current group of students can work together calmly
            if can_work_together(i, j, a, b):
                # Calculate the sum of the skill levels of the current group of students
                current_sum = sum(b[i - 1:j])
                # Update the maximum sum if necessary
                max_sum = max(max_sum, current_sum)
    # Return the maximum sum
    return max_sum

def can_work_together(i, j, a, b):
    # Initialize the result to True
    result = True
    # Iterate over all algorithms
    for k in range(60):
        # Check if the k-th algorithm is known by at least one student in the current group
        if (a[i - 1] >> k) & 1 or (a[j - 1] >> k) & 1:
            # If the k-th algorithm is known by at least one student in the current group,
            # check if it is known by all students in the current group
            if not all((a[i - 1] >> k) & 1 and (a[j - 1] >> k) & 1 for i in range(i, j + 1)):
                # If the k-th algorithm is known by at least one student in the current group,
                # but not all students in the current group know it, the current group cannot work together calmly
                result = False
                break
    # Return the result
    return result


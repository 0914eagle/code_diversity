
def solve(n, order, desired_order):
    # Convert the input permutations to lists
    order = list(map(int, order.split()))
    desired_order = list(map(int, desired_order.split()))
    
    # Check if the input permutations are valid
    if len(order) != n or len(desired_order) != n:
        return "Impossible"
    
    # Initialize a variable to keep track of the number of rotations
    rotations = 0
    
    # Loop through the input permutations and check if they match the desired order
    for i in range(n):
        # If the current position of the bread is not the desired position, rotate the subsequence of breads
        if order[i] != desired_order[i]:
            # Find the index of the first bread in the subsequence that needs to be rotated
            start_index = order.index(desired_order[i])
            # Find the index of the last bread in the subsequence that needs to be rotated
            end_index = start_index + 2
            # Rotate the subsequence of breads
            order = order[:start_index] + order[start_index+1:end_index+1] + order[start_index:start_index+1]
            # Increment the number of rotations
            rotations += 1
    
    # Check if the input permutations match the desired order after all rotations
    if order == desired_order:
        return "Possible"
    else:
        return "Impossible"


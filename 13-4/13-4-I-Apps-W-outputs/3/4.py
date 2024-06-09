
def solve(n, initial_order, target_order):
    # Convert the input permutations to lists
    initial_order = list(map(int, initial_order.split()))
    target_order = list(map(int, target_order.split()))
    
    # Create a copy of the initial order to perform the rotations
    current_order = initial_order[:]
    
    # Iterate through the target order and perform the rotations
    for i in range(n):
        # Find the index of the current element in the current order
        index = current_order.index(target_order[i])
        
        # Rotate the subsequence of length 3 starting from the current index
        current_order = current_order[:index] + current_order[index+1:index+3] + [current_order[index]] + current_order[index+3:]
    
    # Check if the final order is the same as the target order
    if current_order == target_order:
        return "Possible"
    else:
        return "Impossible"


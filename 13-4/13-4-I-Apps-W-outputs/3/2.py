
def is_sortable(bread_order, desired_order):
    # Convert the input permutations to lists
    bread_list = list(map(int, bread_order.split()))
    desired_list = list(map(int, desired_order.split()))
    
    # Check if the bread list is already sorted in the desired order
    if bread_list == desired_list:
        return "Possible"
    
    # Check if the bread list can be sorted by rotating subsequence of length 3
    for i in range(len(bread_list) - 2):
        subsequence = bread_list[i:i+3]
        if subsequence == desired_list[i:i+3]:
            return "Possible"
    
    # If the bread list cannot be sorted, return "Impossible"
    return "Impossible"


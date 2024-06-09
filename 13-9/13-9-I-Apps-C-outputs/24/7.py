
def get_smallest_cluster_size(a_list):
    # Sort the list by the combination of a and b
    sorted_list = sorted(a_list, key=lambda x: x[0] * S + x[1] * T)

    # Initialize the cluster size and the index of the first true value
    cluster_size = 0
    first_true_index = 0

    # Iterate through the sorted list
    for i in range(len(sorted_list)):
        # If the current value is true, update the cluster size and the index of the first true value
        if sorted_list[i][2] == 1:
            cluster_size += 1
            first_true_index = i
        # If the current value is false and the previous value was true, break the loop
        elif sorted_list[i][2] == 0 and sorted_list[i-1][2] == 1:
            break

    # Return the smallest cluster size
    return cluster_size


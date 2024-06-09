
def get_smallest_cluster_size(a, b, c):
    # Sort the data by the measure a*S + b*T
    sorted_data = sorted(zip(a, b, c), key=lambda x: x[0]*S + x[1]*T)

    # Find the indices of the first and last results with c=1
    first_idx = next((i for i, x in enumerate(sorted_data) if x[2] == 1), None)
    last_idx = next((i for i in range(len(sorted_data)-1, -1, -1) if sorted_data[i][2] == 1), None)

    # Return the cluster size
    return last_idx - first_idx + 1


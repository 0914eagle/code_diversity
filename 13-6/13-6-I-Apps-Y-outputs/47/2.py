
def get_nice_indices(arr):
    nice_indices = []
    for i in range(len(arr)):
        sum_of_others = sum(arr) - arr[i]
        if arr[i] == sum_of_others:
            nice_indices.append(i)
    return nice_indices


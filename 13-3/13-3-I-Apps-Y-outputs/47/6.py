
def get_min_sum(arr):
    # Initialize variables
    n = len(arr)
    sum_non_deleted = 0
    parity = 0
    deleted_elements = []

    # Iterate through the array
    for i in range(n):
        # If the current element is not deleted, add it to the sum
        if i not in deleted_elements:
            sum_non_deleted += arr[i]

        # If it's the first move, choose any element and delete it
        if len(deleted_elements) == 0:
            deleted_elements.append(i)
            parity = arr[i] % 2
        # If it's the second or any next move, choose any element with the only restriction: its parity should differ from the parity of the element deleted on the previous move
        else:
            # If the last deleted element was odd, choose any even element and delete it
            if parity == 1:
                for j in range(i+1, n):
                    if arr[j] % 2 == 0 and j not in deleted_elements:
                        deleted_elements.append(j)
                        break
            # If the last deleted element was even, choose any odd element and delete it
            else:
                for j in range(i+1, n):
                    if arr[j] % 2 == 1 and j not in deleted_elements:
                        deleted_elements.append(j)
                        break

    # Return the minimum possible sum of non-deleted elements
    return sum_non_deleted


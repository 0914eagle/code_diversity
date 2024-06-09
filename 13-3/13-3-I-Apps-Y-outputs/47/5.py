
def get_min_sum(arr):
    # Initialize variables
    n = len(arr)
    sum_of_non_deleted_elements = 0
    parity = 0
    deleted_elements = []

    # Iterate through the array
    for i in range(n):
        # If it's the first move, choose any element and delete it
        if i == 0:
            deleted_elements.append(arr[i])
            parity = arr[i] % 2
        # If it's the second or any next move, choose any element with the only restriction: its parity should differ from the parity of the element deleted on the previous move
        else:
            # If the last deleted element was odd, choose any even element and delete it
            if parity == 1:
                for j in range(n):
                    if arr[j] % 2 == 0 and arr[j] not in deleted_elements:
                        deleted_elements.append(arr[j])
                        parity = arr[j] % 2
                        break
            # If the last deleted element was even, choose any odd element and delete it
            else:
                for j in range(n):
                    if arr[j] % 2 == 1 and arr[j] not in deleted_elements:
                        deleted_elements.append(arr[j])
                        parity = arr[j] % 2
                        break

    # Calculate the sum of non-deleted elements
    for i in range(n):
        if arr[i] not in deleted_elements:
            sum_of_non_deleted_elements += arr[i]

    return sum_of_non_deleted_elements


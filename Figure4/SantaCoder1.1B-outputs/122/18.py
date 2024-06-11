def add_elements(arr, k):
    
    # Edge case
    if len(arr) < k:
        return 0

    # Find the two digits of the first k elements
    first_k_digits = arr[:k]
    # Find the two digits of the last k elements
    last_k_digits = arr[-k:]

    # Sum the two digits of the first k elements
    first_k_sum = sum(first_k_digits)

    # Sum the two digits of the last k elements
    last_k_sum = sum(last_k_digits)

    # Return the sum of the two digits of the first k elements
    return first_k_sum + last_k_sum



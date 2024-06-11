def pluck(arr):
    
    if len(arr) == 0:
        return []
    min_even_value = float("inf")
    min_even_value_index = -1
    for i, node in enumerate(arr):
        if node % 2 == 0 and node < min_even_value:
            min_even_value = node
            min_even_value_index = i
    return [min_even_value, min_even_value_index] if min_even_value_index != -1 else []


if __name__ == "__main__":
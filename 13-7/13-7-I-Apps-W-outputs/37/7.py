
def solve(n, k, a, b):
    # Calculate the total taste and total calories of the fruits
    total_taste = sum(a)
    total_calories = sum(b)

    # Initialize the maximum possible sum of the taste values to 0
    max_taste = 0

    # Iterate over all possible combinations of fruits
    for i in range(1, 2**n):
        # Calculate the current combination of fruits
        current_combination = [j for j in range(n) if (i & (1 << j)) > 0]

        # Calculate the current total taste and total calories of the chosen fruits
        current_taste = sum(a[j] for j in current_combination)
        current_calories = sum(b[j] for j in current_combination)

        # Calculate the current taste to calories ratio
        current_ratio = current_taste / current_calories

        # If the current ratio is equal to k and the current combination has at least one fruit, update the maximum possible sum of the taste values
        if current_ratio == k and len(current_combination) > 0:
            max_taste = max(max_taste, current_taste)

    # If no combination of fruits fulfills the condition, return -1
    if max_taste == 0:
        return -1

    # Otherwise, return the maximum possible sum of the taste values
    return max_taste


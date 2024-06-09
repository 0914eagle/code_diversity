
def get_max_taste(n, k, a, b):
    # Sort the fruits by their taste in descending order
    sorted_fruits = sorted(range(n), key=lambda i: a[i], reverse=True)

    # Initialize the maximum taste sum and the current taste sum
    max_taste_sum = 0
    current_taste_sum = 0

    # Iterate through the fruits and choose the ones that follow Inna's principle
    for i in sorted_fruits:
        current_taste_sum += a[i]
        if current_taste_sum * b[i] == k:
            max_taste_sum = current_taste_sum
        elif current_taste_sum * b[i] > k:
            break

    # Return the maximum taste sum
    return max_taste_sum



def fruit_salad(n, k, a, b):
    # Sort the fruits by their taste in descending order
    sorted_fruits = sorted(zip(a, b), key=lambda x: x[0], reverse=True)

    # Initialize the maximum total taste and the chosen fruits
    max_taste = 0
    chosen_fruits = []

    # Iterate through the fruits and choose the ones that satisfy the condition
    for fruit in sorted_fruits:
        taste, calories = fruit
        if calories <= k * (taste - max_taste):
            max_taste += taste
            chosen_fruits.append(fruit)

    # If no fruits were chosen, return -1
    if not chosen_fruits:
        return -1

    # Return the maximum total taste of the chosen fruits
    return sum(fruit[0] for fruit in chosen_fruits)


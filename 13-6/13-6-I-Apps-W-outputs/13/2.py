
def is_possible(n, a):
    # Calculate the total number of pizzas needed
    total_pizzas = sum(a)

    # Initialize the number of pizzas needed for each day
    pizzas_needed = [0] * n

    # Loop through each day
    for i in range(n):
        # Calculate the number of pizzas needed for the current day
        pizzas_needed[i] = a[i]

        # Check if the previous day has any pizzas left over
        if i > 0 and pizzas_needed[i - 1] > 0:
            # Use the coupon to buy one pizza
            pizzas_needed[i] -= 1
            pizzas_needed[i - 1] -= 1

    # Check if all the pizzas have been ordered
    if sum(pizzas_needed) == total_pizzas:
        return "YES"
    else:
        return "NO"


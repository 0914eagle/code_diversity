
def is_possible(n, a):
    # Calculate the total number of pizzas needed
    total_pizzas = sum(a)

    # Initialize the number of pizzas needed for each day
    pizzas_needed = [0] * n

    # Loop through each day
    for i in range(n):
        # If there are teams present on this day, add the number of pizzas needed for this day
        if a[i] > 0:
            pizzas_needed[i] += a[i]

    # Loop through each day
    for i in range(n):
        # If there are teams present on this day and the number of pizzas needed for this day is odd, return "NO"
        if a[i] > 0 and pizzas_needed[i] % 2 == 1:
            return "NO"

    # If the total number of pizzas needed is even, return "YES"
    if total_pizzas % 2 == 0:
        return "YES"
    else:
        # If the total number of pizzas needed is odd, return "NO"
        return "NO"


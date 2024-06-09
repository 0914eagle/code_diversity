
def is_possible(n, a):
    # Initialize the number of pizzas as 0
    pizzas = 0

    # Loop through each day
    for i in range(n):
        # If there are no teams on this day, skip this day
        if a[i] == 0:
            continue

        # If the number of pizzas is already more than the number of teams, return False
        if pizzas > a[i]:
            return False

        # If the number of pizzas is less than the number of teams, add the number of teams to the number of pizzas
        pizzas += a[i]

    # If the number of pizzas is not equal to the total number of teams, return False
    if pizzas != sum(a):
        return False

    # If the number of pizzas is equal to the total number of teams, return True
    return True


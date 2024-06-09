
def get_maximum_identified_colleagues(n, m, a_list):
    # Initialize a list to store the number of burgers ordered on each day
    burger_list = [0] * m

    # Iterate over the list of numbers of burgers ordered on each day
    for i, a in enumerate(a_list):
        # If the number of burgers ordered is greater than the number of salads available, set the number of burgers to the number of salads available
        if a > n - i:
            burger_list[i] = n - i
        # Otherwise, set the number of burgers to the given number
        else:
            burger_list[i] = a

    # Initialize a variable to store the maximum number of colleagues identified
    max_identified = 0

    # Iterate over the list of numbers of burgers ordered on each day
    for i, a in enumerate(burger_list):
        # If the number of burgers ordered is greater than the number of salads available, set the number of salads to the number of salads available
        if a > n - i:
            salad_list = n - i
        # Otherwise, set the number of salads to the number of burgers ordered
        else:
            salad_list = a

        # Update the maximum number of colleagues identified
        max_identified = max(max_identified, salad_list + i)

    return max_identified



def quasibinary_sum(n):
    # Initialize a list to store the quasibinary numbers
    quasibinary_list = []
    # Loop until the sum of the quasibinary numbers is equal to n
    while sum(quasibinary_list) != n:
        # Add the largest quasibinary number that is less than or equal to n to the list
        quasibinary_list.append(min(quasibinary_list + [1], key=lambda x: abs(x - n)))
    # Return the list of quasibinary numbers
    return quasibinary_list


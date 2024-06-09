
def get_quasibinary_sum(n):
    # Initialize a list to store the quasibinary numbers
    quasibinary_numbers = []
    # Loop until the sum of the quasibinary numbers is equal to n
    while sum(quasibinary_numbers) < n:
        # Add the next quasibinary number to the list
        quasibinary_numbers.append(1)
    # Return the list of quasibinary numbers
    return quasibinary_numbers


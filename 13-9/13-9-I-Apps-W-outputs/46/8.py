
def quasibinary_sum(n):
    # Initialize a list to store the quasibinary numbers
    quasibinary_list = []
    
    # Loop until the sum of the quasibinary numbers is equal to n
    while sum(quasibinary_list) < n:
        # Append the next quasibinary number to the list
        quasibinary_list.append(1)
    
    # Return the list of quasibinary numbers
    return quasibinary_list


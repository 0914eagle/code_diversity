
def quasibinary_sum(n):
    # Initialize a list to store the quasibinary numbers
    quasibinary_list = []
    
    # While the sum of the quasibinary numbers is less than or equal to n
    while sum(quasibinary_list) <= n:
        # Append the next quasibinary number to the list
        quasibinary_list.append(1)
    
    # Return the length of the list and the list of quasibinary numbers
    return len(quasibinary_list), quasibinary_list


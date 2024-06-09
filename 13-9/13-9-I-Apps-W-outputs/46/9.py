
def quasibinary_numbers(n):
    # Initialize a list to store the quasibinary numbers
    quasibinary_list = []
    
    # Loop through the numbers from 1 to n
    for i in range(1, n+1):
        # Check if the number is quasibinary
        if is_quasibinary(i):
            # Add the quasibinary number to the list
            quasibinary_list.append(i)
    
    # Return the list of quasibinary numbers
    return quasibinary_list

def is_quasibinary(n):
    # Check if the number is quasibinary
    if n == 0 or n == 1:
        return True
    elif n % 10 == 0 or n % 10 == 1:
        return is_quasibinary(n // 10)
    else:
        return False


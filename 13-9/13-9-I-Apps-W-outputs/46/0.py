
def quasibinary_sum(n):
    # Initialize a list to store the quasibinary numbers
    quasibinary_list = []
    
    # Loop through the numbers from 1 to n
    for i in range(1, n+1):
        # Convert the number to binary and check if it contains only 0s and 1s
        binary_str = bin(i)[2:]
        if binary_str.isdigit() and all(int(i) in [0, 1] for i in binary_str):
            # If the number is quasibinary, add it to the list
            quasibinary_list.append(binary_str)
    
    # Return the list of quasibinary numbers
    return quasibinary_list


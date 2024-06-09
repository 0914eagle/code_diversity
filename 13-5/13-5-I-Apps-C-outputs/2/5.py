
def solve(N, A, B):
    # Calculate the total amount of meat eaten by all participants
    total_meat = sum(A)
    
    # Calculate the amount of ham needed to distribute
    ham_needed = total_meat // N
    
    # Initialize a list to store the amount of ham for each participant
    ham_distributed = [0] * N
    
    # Loop through the participants and distribute the ham
    for i in range(N):
        # If the participant has a non-zero ratio, distribute the ham according to their ratio
        if B[i] != 0:
            ham_distributed[i] = ham_needed * B[i] // sum(B)
    
    # Calculate the total amount of ham distributed
    total_ham = sum(ham_distributed)
    
    # Check if the total amount of ham distributed is equal to the total amount of meat eaten
    if total_ham == total_meat:
        # If it is, return the amount of ham needed to distribute
        return ham_needed
    else:
        # If it's not, return -1 to indicate that the required order cannot be achieved
        return -1


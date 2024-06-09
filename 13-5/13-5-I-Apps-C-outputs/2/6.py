
def solve(N, A, B):
    # Calculate the total amount of meat eaten by all participants
    total_meat = sum(A)
    
    # Calculate the total amount of ham needed to distribute
    total_ham = 0
    for b in B:
        if b != 0:
            total_ham += b
    
    # Calculate the amount of ham needed for each participant
    ham_per_participant = total_ham // N
    
    # Calculate the remaining amount of ham
    remaining_ham = total_ham % N
    
    # Initialize the amount of ham for each participant
    ham_for_each_participant = [0] * N
    
    # Distribute the ham equally among all participants
    for i in range(N):
        ham_for_each_participant[i] = ham_per_participant
    
    # Distribute the remaining ham among the participants with a non-zero ratio
    for i in range(N):
        if B[i] != 0:
            ham_for_each_participant[i] += remaining_ham // sum(B)
    
    # Calculate the total amount of meat eaten by each participant
    total_meat_per_participant = [0] * N
    for i in range(N):
        total_meat_per_participant[i] = A[i] + ham_for_each_participant[i]
    
    # Sort the participants in descending order of meat eaten
    sorted_participants = sorted(range(N), key=lambda k: total_meat_per_participant[k], reverse=True)
    
    # Check if the order is correct
    correct_order = True
    for i in range(N):
        if sorted_participants[i] != i:
            correct_order = False
            break
    
    # If the order is correct, return the total amount of ham needed
    if correct_order:
        return total_ham
    # Otherwise, return -1
    else:
        return -1


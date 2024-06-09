
def solve(N, A, B):
    # Calculate the total amount of meat eaten by all participants
    total_meat = sum(A)
    
    # Calculate the total amount of ham needed to distribute
    total_ham = 0
    for b in B:
        if b != 0:
            total_ham += b
    
    # Check if the total amount of ham is enough to distribute
    if total_ham < total_meat:
        return -1
    
    # Calculate the amount of ham needed for each participant
    ham_per_participant = total_ham // N
    
    # Calculate the remaining amount of ham
    remaining_ham = total_ham % N
    
    # Distribute the ham according to the ratio
    ham_distributed = [0] * N
    for i in range(N):
        if B[i] != 0:
            ham_distributed[i] = ham_per_participant * B[i]
    
    # Distribute the remaining ham equally among the participants with non-zero ratio
    for i in range(remaining_ham):
        for j in range(N):
            if B[j] != 0:
                ham_distributed[j] += 1
                break
    
    # Calculate the total amount of meat eaten by each participant
    total_meat_per_participant = [0] * N
    for i in range(N):
        total_meat_per_participant[i] = A[i] + ham_distributed[i]
    
    # Sort the participants by their total meat eaten
    sorted_participants = sorted(range(N), key=lambda k: total_meat_per_participant[k], reverse=True)
    
    # Check if the order is correct
    correct_order = True
    for i in range(N):
        if sorted_participants[i] != i:
            correct_order = False
            break
    
    # Return the amount of ham needed if the order is correct, -1 otherwise
    if correct_order:
        return total_ham
    else:
        return -1


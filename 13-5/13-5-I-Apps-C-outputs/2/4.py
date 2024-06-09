
def solve(N, A, B):
    # Calculate the total amount of meat eaten by all participants
    total_meat = sum(A)
    
    # Calculate the amount of ham needed to distribute
    ham_needed = total_meat // N
    
    # Calculate the remaining amount of meat after distributing the ham
    remaining_meat = total_meat % N
    
    # Calculate the amount of ham needed for each participant
    ham_per_participant = [ham_needed // N for _ in range(N)]
    
    # Distribute the remaining meat equally among the participants
    for i in range(remaining_meat):
        ham_per_participant[i] += 1
    
    # Sort the participants by the amount of meat eaten
    sorted_participants = sorted(range(N), key=lambda x: A[x], reverse=True)
    
    # Check if the order of the participants is correct
    correct_order = True
    for i in range(N):
        if ham_per_participant[sorted_participants[i]] != B[sorted_participants[i]]:
            correct_order = False
            break
    
    # Return the amount of ham needed if the order is correct, -1 otherwise
    if correct_order:
        return ham_needed
    else:
        return -1


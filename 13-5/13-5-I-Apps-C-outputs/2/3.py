
def solve(N, A, B):
    # Calculate the total amount of meat eaten by all participants
    total_meat = sum(A)
    
    # Calculate the total amount of ham that needs to be distributed
    total_ham = 0
    for b in B:
        if b != 0:
            total_ham += b
    
    # Check if the total amount of ham is divisible by the number of participants
    if total_ham % N != 0:
        return -1
    
    # Calculate the amount of ham each participant should receive
    ham_per_person = total_ham // N
    
    # Calculate the total amount of meat each participant should have eaten
    total_meat_per_person = total_meat // N
    
    # Calculate the amount of meat each participant should have eaten in excess of the total amount per person
    excess_meat = [a - total_meat_per_person for a in A]
    
    # Calculate the amount of ham each participant should receive in excess of the amount per person
    excess_ham = [int(e / total_meat_per_person * ham_per_person) for e in excess_meat]
    
    # Calculate the total amount of ham that needs to be distributed in excess
    total_excess_ham = sum(excess_ham)
    
    # Check if the total amount of ham that needs to be distributed in excess is divisible by the number of participants
    if total_excess_ham % N != 0:
        return -1
    
    # Calculate the amount of ham each participant should receive in excess
    excess_ham_per_person = total_excess_ham // N
    
    # Calculate the total amount of ham that needs to be distributed
    total_ham = ham_per_person * N + excess_ham_per_person * len(excess_ham)
    
    return total_ham


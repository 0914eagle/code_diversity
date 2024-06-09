
def solve(N, A, B):
    # Calculate the total amount of meat eaten by all participants
    total_meat = sum(A)
    
    # Calculate the ratio of ham to be distributed to each participant
    ham_ratio = [ham / total_meat for ham in B]
    
    # Calculate the total amount of ham to be distributed
    total_ham = sum(ham_ratio)
    
    # Check if the required order can be achieved
    if total_ham % 1 != 0:
        return -1
    
    # Calculate the amount of ham to be distributed to each participant
    ham_per_participant = [int(total_ham * ratio) for ratio in ham_ratio]
    
    # Return the total amount of ham to be distributed
    return sum(ham_per_participant)


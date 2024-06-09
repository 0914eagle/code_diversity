
def solve(N, A, B):
    # Calculate the total amount of meat eaten by all participants
    total_meat = sum(A)
    
    # Calculate the ratio of meat eaten by each participant
    ratio = [a / total_meat for a in A]
    
    # Calculate the amount of ham needed to distribute
    ham_needed = sum(b for b in B if b != 0)
    
    # Calculate the amount of ham each participant will receive
    ham_each = [int(ham_needed * r) for r in ratio]
    
    # Check if the order can be achieved
    if all(b == 0 or b == ham_each[i-1] for i, b in enumerate(B, 1)):
        return ham_needed
    else:
        return -1


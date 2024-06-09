
def solve(R, S, L, A, B):
    # Initialize a dictionary to store the number of lawsuits won by each individual and corporation
    wins = {}
    for i in range(1, R+1):
        wins[f"INDV{i}"] = 0
    for i in range(1, S+1):
        wins[f"CORP{i}"] = 0
    
    # Iterate through each lawsuit
    for i in range(L):
        # Get the individual and corporation involved in the lawsuit
        individual = f"INDV{A[i]}"
        corporation = f"CORP{B[i]}"
        
        # If the individual has already won a lawsuit, assign the lawsuit to the corporation
        if wins[individual] > 0:
            wins[corporation] += 1
            print(f"CORP{B[i]}")
        # Otherwise, assign the lawsuit to the individual
        else:
            wins[individual] += 1
            print(f"INDV{A[i]}")
    
    # Return the dictionary of wins
    return wins


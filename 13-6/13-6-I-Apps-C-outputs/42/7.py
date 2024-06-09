
def solve(R, S, L, A, B):
    # Initialize a dictionary to store the number of lawsuits won by each individual and corporation
    wins = {}
    for i in range(1, R+1):
        wins[f"INDV{i}"] = 0
    for i in range(1, S+1):
        wins[f"CORP{i}"] = 0
    
    # Iterate through the lawsuits and update the number of lawsuits won by each individual and corporation
    for i in range(L):
        individual = f"INDV{A[i]}"
        corporation = f"CORP{B[i]}"
        wins[individual] += 1
        wins[corporation] += 1
    
    # Find the individual and corporation with the minimum number of lawsuits won
    min_individual = None
    min_corporation = None
    for individual, count in wins.items():
        if min_individual is None or count < wins[min_individual]:
            min_individual = individual
    for corporation, count in wins.items():
        if min_corporation is None or count < wins[min_corporation]:
            min_corporation = corporation
    
    # Return the ruling for each lawsuit
    ruling = []
    for i in range(L):
        if wins[f"INDV{A[i]}"] < wins[min_individual]:
            ruling.append(f"INDV{A[i]}")
        else:
            ruling.append(f"CORP{B[i]}")
    
    return ruling


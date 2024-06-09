
def solve(R, S, L, lawsuits):
    # Initialize a dictionary to store the number of lawsuits won by each individual and corporation
    counts = {}
    for i in range(1, R+1):
        counts[f"INDV{i}"] = 0
    for i in range(1, S+1):
        counts[f"CORP{i}"] = 0
    
    # Iterate through the lawsuits and update the count for each individual and corporation
    for lawsuit in lawsuits:
        individual, corporation = lawsuit
        counts[f"INDV{individual}"] += 1
        counts[f"CORP{corporation}"] += 1
    
    # Find the individual and corporation with the minimum number of lawsuits won
    min_count = min(counts.values())
    winners = [k for k, v in counts.items() if v == min_count]
    
    # Return the winners for each lawsuit
    return [winners[i%len(winners)] for i in range(L)]


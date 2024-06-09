
def solve(R, S, L, lawsuits):
    # Initialize a dictionary to store the number of lawsuits won by each individual and corporation
    wins = {}
    for i in range(1, R+1):
        wins[f"INDV {i}"] = 0
    for i in range(1, S+1):
        wins[f"CORP {i}"] = 0
    
    # Iterate through the lawsuits and increment the number of lawsuits won by the winning party
    for lawsuit in lawsuits:
        individual, corporation = lawsuit
        if wins[f"INDV {individual}"] < wins[f"CORP {corporation}"]:
            wins[f"INDV {individual}"] += 1
        else:
            wins[f"CORP {corporation}"] += 1
    
    # Find the party with the minimum number of lawsuits won
    min_wins = min(wins.values())
    
    # Return the party with the minimum number of lawsuits won for each lawsuit
    return [key for key, value in wins.items() if value == min_wins]


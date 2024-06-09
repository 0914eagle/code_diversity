
def solve(R, S, L, lawsuits):
    # Initialize a dictionary to store the number of lawsuits won by each individual and corporation
    wins = {}
    for i in range(1, R+1):
        wins[f"INDV {i}"] = 0
    for i in range(1, S+1):
        wins[f"CORP {i}"] = 0
    
    # Iterate through the lawsuits and update the dictionary
    for lawsuit in lawsuits:
        individual, corporation = lawsuit
        wins[f"INDV {individual}"] += 1
        wins[f"CORP {corporation}"] += 1
    
    # Find the individual or corporation with the minimum number of wins
    min_wins = min(wins.values())
    winners = [k for k, v in wins.items() if v == min_wins]
    
    # Return the winners
    return winners


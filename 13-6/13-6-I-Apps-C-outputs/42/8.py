
def solve(R, S, L):
    # Initialize a dictionary to store the number of lawsuits won by each individual and corporation
    wins = {}
    for i in range(1, R+1):
        wins[f"INDV {i}"] = 0
    for i in range(1, S+1):
        wins[f"CORP {i}"] = 0
    
    # Iterate through the lawsuits and increment the number of lawsuits won by each individual and corporation
    for i in range(L):
        indv = f"INDV {input()[0]}"
        corp = f"CORP {input()[1]}"
        wins[indv] += 1
        wins[corp] += 1
    
    # Find the individual or corporation with the minimum number of lawsuits won
    min_wins = min(wins.values())
    for key, value in wins.items():
        if value == min_wins:
            return key


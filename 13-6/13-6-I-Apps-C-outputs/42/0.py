
def solve(R, S, L):
    # Initialize a dictionary to store the number of lawsuits won by each individual and corporation
    wins = {}
    for i in range(1, R+1):
        wins[f"INDV{i}"] = 0
    for i in range(1, S+1):
        wins[f"CORP{i}"] = 0

    # Iterate through the lawsuits and update the dictionary with the winner of each lawsuit
    for i in range(L):
        a, b = map(int, input().split())
        if wins[f"INDV{a}"] < wins[f"CORP{b}"]:
            wins[f"INDV{a}"] += 1
        else:
            wins[f"CORP{b}"] += 1

    # Find the individual or corporation with the minimum number of wins
    min_wins = min(wins.values())

    # Find all individuals or corporations with the minimum number of wins
    winners = [k for k, v in wins.items() if v == min_wins]

    # Randomly select one of the winners to return
    import random
    return random.choice(winners)


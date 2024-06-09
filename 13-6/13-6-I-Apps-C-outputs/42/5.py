
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
    
    # Find the individual or corporation with the minimum number of lawsuits won
    min_wins = min(wins.values())
    for key, value in wins.items():
        if value == min_wins:
            return key

def main():
    R, S, L = map(int, input().split())
    lawsuits = []
    for i in range(L):
        individual, corporation = map(int, input().split())
        lawsuits.append((individual, corporation))
    print(solve(R, S, L, lawsuits))

if __name__ == "__main__":
    main()


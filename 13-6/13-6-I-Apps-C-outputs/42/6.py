
def solve(R, S, L):
    # Initialize a dictionary to store the number of lawsuits won by each individual and corporation
    wins = {}
    for i in range(1, R+1):
        wins[i] = 0
    for i in range(1, S+1):
        wins[i] = 0
    
    # Iterate through the lawsuits and assign the party with the least number of wins to each lawsuit
    for i in range(L):
        # Get the indices of the individual and corporation involved in the lawsuit
        individual = int(input())
        corporation = int(input())
        
        # If the individual has won fewer lawsuits than the corporation, assign the individual to the lawsuit
        if wins[individual] < wins[corporation]:
            print("INDV", individual)
            wins[individual] += 1
        
        # If the corporation has won fewer lawsuits than the individual, assign the corporation to the lawsuit
        elif wins[corporation] < wins[individual]:
            print("CORP", corporation)
            wins[corporation] += 1
        
        # If both the individual and corporation have the same number of wins, assign the individual to the lawsuit
        else:
            print("INDV", individual)
            wins[individual] += 1
    
    return wins


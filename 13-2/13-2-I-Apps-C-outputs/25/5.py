
import itertools

def f1(n, m, d):
    # Calculate the probability of removing all opponent's minions
    # using the "Explosion" spell
    
    # Initialize the probability to 0
    probability = 0
    
    # Iterate over all possible combinations of minion healths
    for my_minions in itertools.product(range(1, 7), repeat=n):
        for opp_minions in itertools.product(range(1, 7), repeat=m):
            # Calculate the number of minions that will be removed
            # by the "Explosion" spell
            num_removed = 0
            for i in range(d):
                # Find the index of the minion that will receive the next unit of damage
                idx = i % m
                if opp_minions[idx] - 1 <= 0:
                    # If the minion's health is already 0, skip it
                    continue
                else:
                    # Decrease the minion's health by 1
                    opp_minions = list(opp_minions)
                    opp_minions[idx] -= 1
                    num_removed += 1
            
            # If all opponent's minions are removed, add the probability to the total
            if num_removed == m:
                probability += 1 / (n * m)
    
    return probability

def f2(n, m, d):
    # Calculate the probability of removing all opponent's minions
    # using the "Explosion" spell, assuming that all your own minions
    # will be removed as well
    
    # Initialize the probability to 0
    probability = 0
    
    # Iterate over all possible combinations of minion healths
    for my_minions in itertools.product(range(1, 7), repeat=n):
        for opp_minions in itertools.product(range(1, 7), repeat=m):
            # Calculate the number of minions that will be removed
            # by the "Explosion" spell
            num_removed = 0
            for i in range(d):
                # Find the index of the minion that will receive the next unit of damage
                idx = i % m
                if opp_minions[idx] - 1 <= 0:
                    # If the minion's health is already 0, skip it
                    continue
                else:
                    # Decrease the minion's health by 1
                    opp_minions = list(opp_minions)
                    opp_minions[idx] -= 1
                    num_removed += 1
            
            # If all opponent's minions are removed, add the probability to the total
            if num_removed == m:
                probability += 1 / (n * m)
    
    return probability

if __name__ == '__main__':
    n, m, d = map(int, input().split())
    print(f1(n, m, d))
    print(f2(n, m, d))


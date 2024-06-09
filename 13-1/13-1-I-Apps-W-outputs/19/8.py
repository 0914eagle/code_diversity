
import itertools

def f1(R, G, B, Y, S):
    # Calculate the probability of the players winning
    prob_win = 0
    
    # Iterate over all possible combinations of fruit picks and raven movements
    for picks in itertools.product(range(R+1), range(G+1), range(B+1), range(Y+1)):
        # Calculate the number of fruits left in the basket after each pick
        fruits_left = sum(picks)
        
        # Calculate the number of steps the raven needs to take to reach the orchard
        raven_steps = min(S, fruits_left)
        
        # If the raven reaches the orchard before the players have placed all fruits into the basket, the players lose
        if raven_steps < fruits_left:
            prob_win += 1 / (R*G*B*Y)
    
    return prob_win

def f2(...):
    # Calculate the probability of the players winning
    prob_win = 0
    
    # Iterate over all possible combinations of fruit picks and raven movements
    for picks in itertools.product(range(R+1), range(G+1), range(B+1), range(Y+1)):
        # Calculate the number of fruits left in the basket after each pick
        fruits_left = sum(picks)
        
        # Calculate the number of steps the raven needs to take to reach the orchard
        raven_steps = min(S, fruits_left)
        
        # If the raven reaches the orchard before the players have placed all fruits into the basket, the players lose
        if raven_steps < fruits_left:
            prob_win += 1 / (R*G*B*Y)
    
    return prob_win

if __name__ == '__main__':
    R, G, B, Y, S = map(int, input().split())
    print(f1(R, G, B, Y, S))


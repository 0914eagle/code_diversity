
import itertools

def f1(R, G, B, Y, S):
    # Calculate the probability of the players winning
    prob_win = 0
    
    # Iterate over all possible combinations of fruit picks and raven moves
    for picks, raven in itertools.product(range(R+1), range(G+1), range(B+1), range(Y+1), range(S+1)):
        # Calculate the number of fruits left in the basket after each pick
        basket = picks[0] + picks[1] + picks[2] + picks[3]
        
        # If the raven reaches the orchard before the players have placed all fruits into the basket, the players lose
        if raven == S:
            prob_win += 0
        
        # If the players have placed all fruits into the basket, they win
        elif basket == R+G+B+Y:
            prob_win += 1
    
    # Return the probability of the players winning
    return prob_win / (R+G+B+Y)**4

def f2(...):
    # Calculate the probability of the players winning
    prob_win = 0
    
    # Iterate over all possible combinations of fruit picks and raven moves
    for picks, raven in itertools.product(range(R+1), range(G+1), range(B+1), range(Y+1), range(S+1)):
        # Calculate the number of fruits left in the basket after each pick
        basket = picks[0] + picks[1] + picks[2] + picks[3]
        
        # If the raven reaches the orchard before the players have placed all fruits into the basket, the players lose
        if raven == S:
            prob_win += 0
        
        # If the players have placed all fruits into the basket, they win
        elif basket == R+G+B+Y:
            prob_win += 1
    
    # Return the probability of the players winning
    return prob_win / (R+G+B+Y)**4

if __name__ == '__main__':
    R, G, B, Y, S = map(int, input().split())
    print(f1(R, G, B, Y, S))


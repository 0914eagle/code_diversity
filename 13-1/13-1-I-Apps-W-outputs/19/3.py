
import itertools

def f1(R, G, B, Y, S):
    # Calculate the probability of the players winning
    prob_win = 0
    
    # Iterate over all possible combinations of fruit picks and raven moves
    for fruit_pick, raven_move in itertools.product(range(R+1), range(G+1), range(B+1), range(Y+1)):
        # Calculate the number of fruits left on each tree after the players make their picks
        r_left = R - fruit_pick
        g_left = G - fruit_pick
        b_left = B - fruit_pick
        y_left = Y - fruit_pick
        
        # Calculate the number of steps the raven moves
        raven_steps = raven_move
        
        # Check if the players have picked all fruits before the raven reaches the orchard
        if r_left == 0 and g_left == 0 and b_left == 0 and y_left == 0:
            # If the players have picked all fruits, they win
            prob_win += 1
        elif raven_steps == S:
            # If the raven reaches the orchard, the players lose
            pass
        else:
            # If the players have not picked all fruits and the raven has not reached the orchard,
            # calculate the probability of the players winning in the next turn
            prob_win += f1(r_left, g_left, b_left, y_left, raven_steps+1)
    
    # Return the probability of the players winning
    return prob_win

def f2(...):
    # Calculate the probability of the players winning
    prob_win = 0
    
    # Iterate over all possible combinations of fruit picks and raven moves
    for fruit_pick, raven_move in itertools.product(range(R+1), range(G+1), range(B+1), range(Y+1)):
        # Calculate the number of fruits left on each tree after the players make their picks
        r_left = R - fruit_pick
        g_left = G - fruit_pick
        b_left = B - fruit_pick
        y_left = Y - fruit_pick
        
        # Calculate the number of steps the raven moves
        raven_steps = raven_move
        
        # Check if the players have picked all fruits before the raven reaches the orchard
        if r_left == 0 and g_left == 0 and b_left == 0 and y_left == 0:
            # If the players have picked all fruits, they win
            prob_win += 1
        elif raven_steps == S:
            # If the raven reaches the orchard, the players lose
            pass
        else:
            # If the players have not picked all fruits and the raven has not reached the orchard,
            # calculate the probability of the players winning in the next turn
            prob_win += f2(r_left, g_left, b_left, y_left, raven_steps+1)
    
    # Return the probability of the players winning
    return prob_win

if __name__ == '__main__':
    R, G, B, Y, S = map(int, input().split())
    print(f1(R, G, B, Y, S))


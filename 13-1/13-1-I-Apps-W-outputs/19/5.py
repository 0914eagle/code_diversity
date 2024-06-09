
import itertools

def f1(R, G, B, Y, S):
    # Initialize the probability of winning as 0
    prob = 0

    # Iterate over all possible combinations of fruit picks and raven movements
    for picks in itertools.product(range(R+1), range(G+1), range(B+1), range(Y+1)):
        # Calculate the number of fruits left in the basket after each pick
        basket = sum(picks)

        # Calculate the number of steps the raven needs to take to reach the orchard
        raven = min(basket, S)

        # If the raven reaches the orchard before the players have placed all fruits into the basket, the players lose
        if raven == S:
            continue

        # Calculate the probability of winning after each pick
        prob += (1 / (R+1)**4) * (1 / (G+1)**4) * (1 / (B+1)**4) * (1 / (Y+1)**4)

    # Return the probability of winning
    return prob

def f2(...):
    # Your code here

if __name__ == '__main__':
    R, G, B, Y, S = map(int, input().split())
    print(f1(R, G, B, Y, S))


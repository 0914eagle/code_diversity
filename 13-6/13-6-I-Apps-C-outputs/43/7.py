
import math

def f1(N, H, p, v):
    # Initialize the expected payout
    expected_payout = 0
    
    # Loop through each hole
    for i in range(H):
        # Calculate the probability of falling into the hole
        probability = p[i]
        
        # Calculate the expected payout if the ball falls into the hole
        expected_payout_hole = v[i]
        
        # Calculate the expected payout if the ball bounces to a neighbor
        expected_payout_neighbor = 0
        for j in range(4):
            if p[i * 5 + j + 1] > 0:
                expected_payout_neighbor += p[i * 5 + j + 1] * f1(N, H, p[i * 5 + j + 1:], v)
        
        # Calculate the total expected payout for this hole
        expected_payout += probability * (expected_payout_hole + expected_payout_neighbor)
    
    return expected_payout

def f2(N, H, p, v):
    # Initialize the expected payout
    expected_payout = 0
    
    # Loop through each hole
    for i in range(H):
        # Calculate the probability of falling into the hole
        probability = p[i]
        
        # Calculate the expected payout if the ball falls into the hole
        expected_payout_hole = v[i]
        
        # Calculate the expected payout if the ball bounces to a neighbor
        expected_payout_neighbor = 0
        for j in range(4):
            if p[i * 5 + j + 1] > 0:
                expected_payout_neighbor += p[i * 5 + j + 1] * f2(N, H, p[i * 5 + j + 1:], v)
        
        # Calculate the total expected payout for this hole
        expected_payout += probability * (expected_payout_hole + expected_payout_neighbor)
    
    return expected_payout

if __name__ == '__main__':
    N = int(input())
    H = int(input())
    p = [float(i) for i in input().split()]
    v = [int(i) for i in input().split()]
    
    # Calculate the expected payout
    expected_payout = f1(N, H, p, v)
    
    # Print the expected payout
    print(expected_payout)



def solve(n, k, s):
    # Initialize the number of moves
    moves = 0
    
    # Initialize the number of color sides facing up
    num_up = s.count('1')
    
    # Initialize the number of color sides facing down
    num_down = n - num_up
    
    # Initialize the number of moves to flip all color sides to the same direction
    num_flips = num_up if num_up > num_down else num_down
    
    # Loop until all color sides are facing the same direction or the total number of moves exceeds 10^9
    while num_up != num_down and moves < 10**9:
        # If the number of moves to flip all color sides to the same direction is even, flip all color sides up
        if num_flips % 2 == 0:
            num_up = n
            num_down = 0
        # If the number of moves to flip all color sides to the same direction is odd, flip all color sides down
        else:
            num_up = 0
            num_down = n
        
        # Increment the number of moves
        moves += 1
    
    # If the total number of moves exceeds 10^9, return "once again"
    if moves >= 10**9:
        return "once again"
    # If Tokitsukaze will win, return "tokitsukaze"
    elif num_up > num_down:
        return "tokitsukaze"
    # If Quailty will win, return "quailty"
    else:
        return "quailty"

def main():
    n, k = map(int, input().split())
    s = input()
    print(solve(n, k, s))

if __name__ == '__main__':
    main()


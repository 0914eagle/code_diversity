
def f1(n):
    # Initialize variables
    moves = 0
    divisible = False
    
    # Loop until the number is divisible by 25 or the maximum number of moves is reached
    while not divisible and moves < 100:
        # Check if the number is already divisible by 25
        if n % 25 == 0:
            divisible = True
            break
        
        # Swap the last two digits of the number
        n = int(str(n)[:-1] + str(n)[-1] + str(n)[-2])
        moves += 1
    
    # Return the minimum number of moves required to obtain a number divisible by 25, or -1 if it is impossible
    if divisible:
        return moves
    else:
        return -1


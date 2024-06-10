
def solve(n, k, cards):
    # Initialize the number of moves to 0
    moves = 0
    
    # Loop through each card
    for i in range(n):
        # If the card is facing up, add the number of moves to the total
        if cards[i] == "1":
            moves += 1
    
    # If the total number of moves is less than or equal to k, return "tokitsukaze"
    if moves <= k:
        return "tokitsukaze"
    
    # If the total number of moves is greater than k, return "quailty"
    elif moves > k:
        return "quailty"
    
    # If the total number of moves is equal to 10^9, return "once again"
    else:
        return "once again"
    
def main():
    n, k = map(int, input().split())
    cards = input()
    print(solve(n, k, cards))
    
if __name__ == '__main__':
    main()


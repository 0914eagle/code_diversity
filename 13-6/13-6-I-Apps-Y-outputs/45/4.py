
def get_min_moves(n):
    # Initialize the minimum number of moves to -1
    min_moves = -1
    
    # Loop through each possible move
    for i in range(len(n) - 1):
        # Get the current digit
        curr_digit = n[i]
        
        # Get the next digit
        next_digit = n[i + 1]
        
        # Check if the current digit is 0
        if curr_digit == "0":
            # If the current digit is 0, skip this move
            continue
        
        # Check if the next digit is 0
        if next_digit == "0":
            # If the next digit is 0, skip this move
            continue
        
        # Check if the current digit is 5
        if curr_digit == "5":
            # If the current digit is 5, skip this move
            continue
        
        # Check if the next digit is 5
        if next_digit == "5":
            # If the next digit is 5, skip this move
            continue
        
        # Check if the current digit is even
        if curr_digit % 2 == 0:
            # If the current digit is even, skip this move
            continue
        
        # Check if the next digit is even
        if next_digit % 2 == 0:
            # If the next digit is even, skip this move
            continue
        
        # If the current digit is odd and the next digit is odd,
        # then we can swap the digits and make the number divisible by 5
        min_moves = 1
        break
    
    return min_moves

def main():
    n = input("Enter a number: ")
    print(get_min_moves(n))

if __name__ == '__main__':
    main()


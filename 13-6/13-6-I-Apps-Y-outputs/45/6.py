
def get_min_moves(n):
    # Initialize the minimum number of moves to -1
    min_moves = -1
    
    # Loop through each digit in the number
    for i in range(len(n)):
        # Get the current digit
        curr_digit = n[i]
        
        # Check if the current digit is 0
        if curr_digit == "0":
            # If the current digit is 0, continue to the next digit
            continue
        
        # Get the previous digit
        prev_digit = n[i-1] if i > 0 else ""
        
        # Get the next digit
        next_digit = n[i+1] if i < len(n)-1 else ""
        
        # Check if the previous digit is not 0 and the next digit is not 0
        if prev_digit != "0" and next_digit != "0":
            # If both the previous and next digits are not 0, swap them
            n = n[:i] + next_digit + prev_digit + n[i+2:]
            min_moves += 1
    
    # Check if the number is divisible by 25
    if int(n) % 25 == 0:
        # If the number is divisible by 25, return the minimum number of moves
        return min_moves
    else:
        # If the number is not divisible by 25, return -1
        return -1

def main():
    n = input("Enter a number: ")
    print(get_min_moves(n))

if __name__ == '__main__':
    main()


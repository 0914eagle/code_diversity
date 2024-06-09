
def get_min_moves(n):
    # Initialize the minimum number of moves to -1
    min_moves = -1
    
    # Loop through each digit in the number
    for i in range(len(n)):
        # Check if the current digit is 0
        if n[i] == '0':
            # If it is, continue to the next digit
            continue
        # If the current digit is not 0, check if the previous digit is 0
        if i > 0 and n[i-1] == '0':
            # If it is, continue to the next digit
            continue
        # If the current digit is not 0 and the previous digit is not 0, check if the number is divisible by 25
        if int(n) % 25 == 0:
            # If it is, return the minimum number of moves
            return min_moves
        # If the number is not divisible by 25, increment the minimum number of moves
        min_moves += 1
    
    # If the minimum number of moves is still -1, return -1
    return min_moves

def main():
    n = input()
    print(get_min_moves(n))

if __name__ == '__main__':
    main()


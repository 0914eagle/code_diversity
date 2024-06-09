
def get_min_moves(n):
    # Initialize the minimum number of moves to -1
    min_moves = -1
    
    # Loop through each digit in the number
    for i in range(len(n)):
        # If the current digit is not a 0 or 5, skip this digit
        if n[i] not in ["0", "5"]:
            continue
        
        # If the current digit is a 0, try swapping it with the next digit
        if n[i] == "0":
            # If the next digit is a 5, swap them and update the minimum number of moves
            if n[i+1] == "5":
                min_moves = 1
                break
        
        # If the current digit is a 5, try swapping it with the previous digit
        if n[i] == "5":
            # If the previous digit is a 0, swap them and update the minimum number of moves
            if n[i-1] == "0":
                min_moves = 1
                break
    
    # Return the minimum number of moves
    return min_moves

def main():
    # Read a single integer n from stdin
    n = int(input())
    
    # Call the get_min_moves function and print the result
    print(get_min_moves(n))

if __name__ == '__main__':
    main()


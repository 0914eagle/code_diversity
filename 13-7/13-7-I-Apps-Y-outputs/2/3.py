
def get_min_moves(n):
    # Initialize the minimum number of moves to -1
    min_moves = -1
    
    # Loop through each digit in the number
    for i in range(len(n)):
        # If the current digit is 0, skip it
        if n[i] == '0':
            continue
        # If the current digit is 5, check if the next digit is 0
        if n[i] == '5' and i < len(n) - 1 and n[i+1] == '0':
            # If the next digit is 0, set the minimum number of moves to 1
            min_moves = 1
            break
        # If the current digit is not 5, check if the next digit is 5
        if n[i] != '5' and i < len(n) - 1 and n[i+1] == '5':
            # If the next digit is 5, set the minimum number of moves to 2
            min_moves = 2
            break
    
    # Return the minimum number of moves
    return min_moves

def get_resulting_number(n, min_moves):
    # Initialize the resulting number to the original number
    result = n
    
    # Loop through each digit in the number
    for i in range(len(n)):
        # If the current digit is 0, skip it
        if n[i] == '0':
            continue
        # If the current digit is 5, check if the next digit is 0
        if n[i] == '5' and i < len(n) - 1 and n[i+1] == '0':
            # If the next digit is 0, swap the current digit with the next digit
            result = result[:i] + result[i+1] + result[i] + result[i+2:]
            break
        # If the current digit is not 5, check if the next digit is 5
        if n[i] != '5' and i < len(n) - 1 and n[i+1] == '5':
            # If the next digit is 5, swap the current digit with the next digit
            result = result[:i] + result[i+1] + result[i] + result[i+2:]
            break
    
    # Return the resulting number
    return result

def main():
    # Read a single integer from stdin and convert it to a string
    n = input().strip()
    
    # Call the get_min_moves function to get the minimum number of moves
    min_moves = get_min_moves(n)
    
    # If the minimum number of moves is -1, print -1
    if min_moves == -1:
        print(-1)
    # Otherwise, call the get_resulting_number function to get the resulting number
    else:
        result = get_resulting_number(n, min_moves)
        print(result)

if __name__ == '__main__':
    main()


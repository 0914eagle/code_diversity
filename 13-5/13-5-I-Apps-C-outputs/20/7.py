
def get_best_friend_pairs(n):
    # Initialize a list to store the best friend pairs
    best_friend_pairs = []
    
    # Iterate from 10^n-1 to 10^n
    for i in range(10**n-1, 10**n):
        # Initialize a list to store the digits of i
        digits = [int(d) for d in str(i)]
        
        # Initialize a list to store the digits of the best friend pair
        best_friend_pair = []
        
        # Iterate through the digits of i
        for j in range(n):
            # If the digit is 0 or 9, add 1 to it
            if digits[j] in [0, 9]:
                best_friend_pair.append(digits[j] + 1)
            # If the digit is 1, subtract 1 from it
            elif digits[j] == 1:
                best_friend_pair.append(digits[j] - 1)
            # If the digit is between 2 and 8, add or subtract 1 from it
            else:
                best_friend_pair.append(digits[j] + 1 if j % 2 == 0 else digits[j] - 1)
        
        # Add the best friend pair to the list of best friend pairs
        best_friend_pairs.append(int("".join(map(str, best_friend_pair))))
    
    # Return the number of best friend pairs
    return len(set(best_friend_pairs))

def main():
    # Read the input n
    n = int(input())
    
    # Call the function to get the number of best friend pairs
    result = get_best_friend_pairs(n)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()


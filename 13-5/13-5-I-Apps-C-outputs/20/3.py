
def get_best_friend_pairs(n):
    # Initialize a set to store the best friend pairs
    best_friend_pairs = set()
    
    # Iterate over all possible numbers with n digits
    for x in range(10**n):
        # Convert the number to a string
        x_str = str(x)
        
        # Iterate over all possible positions to apply the friendly operation
        for i in range(n-1):
            # Get the two adjacent digits
            d1 = int(x_str[i])
            d2 = int(x_str[i+1])
            
            # Apply the friendly operation
            if d1 + d2 <= 9:
                d1 += 1
                d2 += 1
            elif d1 - d2 >= 1:
                d1 -= 1
                d2 -= 1
            
            # Convert the digits back to a number
            y = int(x_str[:i] + str(d1) + str(d2) + x_str[i+2:])
            
            # If the new number is valid and not already in the set, add it to the set
            if y >= 10**(n-1) and y < 10**n and y not in best_friend_pairs:
                best_friend_pairs.add(y)
    
    # Return the number of pairs in the set
    return len(best_friend_pairs)

def main():
    n = int(input())
    print(get_best_friend_pairs(n))

if __name__ == '__main__':
    main()


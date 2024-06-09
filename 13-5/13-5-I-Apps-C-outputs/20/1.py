
import math

def get_best_friend_pairs(n):
    # Initialize a list to store the best friend pairs
    best_friend_pairs = []
    
    # Iterate from 10^n-1 to 10^n
    for i in range(int(math.pow(10, n)), int(math.pow(10, n+1))):
        # Initialize a list to store the numbers that are best friends with i
        best_friends = []
        
        # Iterate from 1 to 9
        for j in range(1, 10):
            # Calculate the new number by applying the friendly operation on i and j
            new_number = apply_friendly_operation(i, j)
            
            # If the new number is valid and not already in the list of best friends, add it to the list
            if new_number > 0 and new_number not in best_friends:
                best_friends.append(new_number)
        
        # Add the list of best friends to the list of best friend pairs
        best_friend_pairs.append(best_friends)
    
    # Return the number of pairs of best friend numbers with exactly n digits
    return len(best_friend_pairs)

def apply_friendly_operation(x, y):
    # Calculate the sum of the two adjacent digits of x
    sum_of_adjacent_digits = int(str(x)[y-1] + str(x)[y])
    
    # Calculate the difference of the two adjacent digits of x
    difference_of_adjacent_digits = int(str(x)[y-1]) - int(str(x)[y])
    
    # If the sum of the two adjacent digits is equal to y, return the new number
    if sum_of_adjacent_digits == y:
        return x + 1
    # If the difference of the two adjacent digits is equal to y, return the new number
    elif difference_of_adjacent_digits == y:
        return x - 1
    # Otherwise, return 0
    else:
        return 0

if __name__ == '__main__':
    n = int(input())
    print(get_best_friend_pairs(n))



def get_best_friend_pairs(n):
    # Initialize a list to store the best friend pairs
    best_friend_pairs = []
    
    # Iterate from 10^n-1 to 10^n
    for i in range(10**n-1, 10**n):
        # Check if the number is a best friend pair with itself
        if is_best_friend_pair(i, i):
            best_friend_pairs.append(i)
    
    # Return the number of best friend pairs
    return len(best_friend_pairs)

def is_best_friend_pair(x, y):
    # Check if x and y have the same length
    if len(str(x)) != len(str(y)):
        return False
    
    # Initialize a set to store the visited numbers
    visited = set()
    
    # Initialize a queue to store the numbers to be processed
    queue = [x]
    
    # Loop until the queue is empty
    while queue:
        # Dequeue a number from the queue
        num = queue.pop(0)
        
        # Check if the number is already visited
        if num in visited:
            continue
        
        # Add the number to the visited set
        visited.add(num)
        
        # Check if the number is equal to y
        if num == y:
            return True
        
        # Enqueue the friendly numbers of the number
        queue.extend(get_friendly_numbers(num))
    
    # If the queue is empty and y is not in the visited set, then x and y are not a best friend pair
    return False

def get_friendly_numbers(num):
    # Initialize a list to store the friendly numbers
    friendly_numbers = []
    
    # Iterate over the digits of the number
    for i in range(len(str(num))):
        # Get the digit at position i
        digit = int(str(num)[i])
        
        # Check if the digit is not 0 or 9
        if digit != 0 and digit != 9:
            # Add the friendly numbers to the list
            friendly_numbers.append(num + 10**i)
            friendly_numbers.append(num - 10**i)
    
    # Return the list of friendly numbers
    return friendly_numbers

if __name__ == '__main__':
    n = int(input())
    print(get_best_friend_pairs(n))


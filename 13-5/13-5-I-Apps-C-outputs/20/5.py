
def get_best_friend_pairs(n):
    # Initialize a list to store the best friend pairs
    best_friend_pairs = []
    
    # Iterate from 10^n to 10^n - 1
    for i in range(10**n, 10**(n-1), -1):
        # Check if the number is a best friend pair
        if is_best_friend_pair(i):
            # Add the number to the list of best friend pairs
            best_friend_pairs.append(i)
    
    # Return the list of best friend pairs
    return best_friend_pairs

def is_best_friend_pair(num):
    # Initialize a set to store the numbers that have been processed
    processed_nums = set()
    
    # Initialize a queue to store the numbers to be processed
    queue = [num]
    
    # Loop until the queue is empty
    while queue:
        # Get the first number from the queue
        curr_num = queue.pop(0)
        
        # Check if the number has already been processed
        if curr_num in processed_nums:
            # If the number has already been processed, return False
            return False
        
        # Add the number to the set of processed numbers
        processed_nums.add(curr_num)
        
        # Get the adjacent digits of the number
        digit1, digit2 = str(curr_num)[0], str(curr_num)[1]
        
        # Check if the number can be obtained by applying the friendly operation
        if digit1 == "0" or digit2 == "9":
            # If the number cannot be obtained by applying the friendly operation, return False
            return False
        
        # Get the new number by applying the friendly operation
        new_num = int(str(curr_num)[1:] + str(int(digit1) + int(digit2)))
        
        # Add the new number to the queue
        queue.append(new_num)
    
    # If the queue is empty, return True
    return True

def main():
    # Read the input n
    n = int(input())
    
    # Get the list of best friend pairs
    best_friend_pairs = get_best_friend_pairs(n)
    
    # Print the number of best friend pairs
    print(len(best_friend_pairs))

if __name__ == '__main__':
    main()


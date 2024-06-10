
def get_number_of_possible_orders(n, a):
    # Initialize a dictionary to store the number of possible orders for each person
    num_orders = {i: 0 for i in range(1, n + 1)}
    
    # Initialize a set to store the people who have been processed
    processed = set()
    
    # Iterate through the input array and update the number of possible orders for each person
    for i in range(n):
        # If the person has already been processed, skip them
        if i in processed:
            continue
        
        # Initialize a queue to store the people who are standing to the left of the current person
        queue = [i]
        
        # Iterate through the queue and update the number of possible orders for each person
        while queue:
            # Pop a person from the queue
            person = queue.pop(0)
            
            # If the person has already been processed, skip them
            if person in processed:
                continue
            
            # Update the number of possible orders for the current person
            num_orders[person] += 1
            
            # Add the people standing to the left and right of the current person to the queue
            queue.extend([person - 1, person + 1])
            
            # Mark the current person as processed
            processed.add(person)
    
    # Return the sum of the number of possible orders for all people
    return sum(num_orders.values()) % 1000000007

def main():
    # Read the input data
    n = int(input())
    a = list(map(int, input().split()))
    
    # Call the function to find the number of possible orders
    result = get_number_of_possible_orders(n, a)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()


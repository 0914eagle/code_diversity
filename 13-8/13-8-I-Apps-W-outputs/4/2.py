
def get_message_count(messages, k):
    # Initialize a set to store the seen messages
    seen = set()
    # Initialize a queue to store the messages to process
    queue = []
    
    # Add the first message to the queue
    queue.append(messages[0])
    
    # Loop until the queue is empty
    while queue:
        # Get the current message from the queue
        message = queue.pop(0)
        
        # If the message has not been seen before, add it to the seen set and add its previous message (if any) to the queue
        if message not in seen:
            seen.add(message)
            if message > 0:
                queue.append(message - 1)
        
        # Add the current message's previous and next messages (if any) to the queue
        if message - k >= 0:
            queue.append(message - k)
        if message + k < len(messages):
            queue.append(message + k)
    
    # Return the number of distinct messages seen
    return len(seen)

def main():
    # Read the input n and k
    n, k = map(int, input().split())
    
    # Read the message links
    messages = list(map(int, input().split()))
    
    # Call the get_message_count function for each message
    counts = [get_message_count(messages, k) for message in range(1, n + 1)]
    
    # Print the counts
    print(*counts, sep='\n')

if __name__ == '__main__':
    main()


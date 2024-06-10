
def get_messages_to_read(n, k, links):
    # Initialize a set to store the messages that have been read
    read_messages = set()
    
    # Initialize a queue to store the messages to process
    queue = [1]
    
    # Loop until the queue is empty
    while queue:
        # Get the current message from the queue
        message = queue.pop(0)
        
        # If the message has not been read already, read it and add it to the set of read messages
        if message not in read_messages:
            read_messages.add(message)
        
        # If the current message has a link, add the linked message to the queue
        if links[message-1] != 0:
            queue.append(links[message-1])
        
        # If the queue length is equal to k, break the loop
        if len(queue) == k:
            break
    
    # Return the number of distinct messages that have been read
    return len(read_messages)

def main():
    # Read the input n, k, and links from stdin
    n, k = map(int, input().split())
    links = list(map(int, input().split()))
    
    # Call the get_messages_to_read function to get the number of messages to read for each message
    messages_to_read = [get_messages_to_read(n, k, links) for i in range(1, n+1)]
    
    # Print the number of messages to read for each message
    print(*messages_to_read)

if __name__ == '__main__':
    main()


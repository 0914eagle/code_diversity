
def read_messages(n, k, messages):
    # Initialize a set to store the read messages
    read_messages = set()
    # Initialize a queue to store the messages to be read
    queue = []
    # Add the starting message to the queue
    queue.append(n)
    # Loop until the queue is empty
    while queue:
        # Get the current message from the queue
        message = queue.pop(0)
        # If the message has not been read already, read it and add it to the set of read messages
        if message not in read_messages:
            read_messages.add(message)
            # If the message has a link, add the link to the queue
            if messages[message] != 0:
                queue.append(messages[message])
    # Return the number of distinct messages read
    return len(read_messages)

def main():
    # Read the input
    n, k = map(int, input().split())
    messages = list(map(int, input().split()))
    # Call the read_messages function for each message
    results = [read_messages(i, k, messages) for i in range(1, n+1)]
    # Print the results
    print(*results, sep='\n')

if __name__ == '__main__':
    main()


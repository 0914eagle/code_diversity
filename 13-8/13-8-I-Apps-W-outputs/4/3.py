
def read_messages(messages, k):
    # Initialize a set to store the read messages
    read_messages = set()
    # Initialize a queue to store the messages to be processed
    queue = []
    # Add the first message to the queue
    queue.append(messages[0])
    # Loop until the queue is empty
    while queue:
        # Get the current message from the queue
        message = queue.pop(0)
        # If the message has not been read already, mark it as read and add it to the set of read messages
        if message not in read_messages:
            read_messages.add(message)
            # If the message has a link, add the link to the queue
            if message in messages:
                queue.append(messages[message])
    # Return the number of distinct messages read
    return len(read_messages)

def main():
    # Read the input
    n, k = map(int, input().split())
    messages = list(map(int, input().split()))
    # Initialize the output array
    output = [0] * (n + 1)
    # Loop through each message
    for i in range(1, n + 1):
        # Calculate the number of distinct messages read starting from message i
        output[i] = read_messages(messages[:i], k)
    # Print the output
    print(*output, sep='\n')

if __name__ == '__main__':
    main()


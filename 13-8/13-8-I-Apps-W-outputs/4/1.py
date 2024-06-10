
def get_number_of_distinct_messages(messages, k):
    # Initialize a set to store the seen messages
    seen = set()
    # Initialize a queue to store the messages to be processed
    queue = []
    # Add the first message to the queue
    queue.append(messages[0])
    # Loop until the queue is empty
    while queue:
        # Get the current message from the queue
        message = queue.pop(0)
        # If the message is not in the seen set, add it to the seen set and the number of distinct messages
        if message not in seen:
            seen.add(message)
        # If the message has a link, add the linked message to the queue
        if messages[message]:
            queue.append(messages[message])
    # Return the number of distinct messages
    return len(seen)

def main():
    # Read the input n and k
    n, k = map(int, input().split())
    # Read the message links
    messages = list(map(int, input().split()))
    # Initialize the number of distinct messages for each message
    number_of_distinct_messages = [0] * (n + 1)
    # Loop through each message
    for i in range(1, n + 1):
        # Get the number of distinct messages for the current message
        number_of_distinct_messages[i] = get_number_of_distinct_messages(messages, k)
    # Print the number of distinct messages for each message
    print(*number_of_distinct_messages, sep='\n')

if __name__ == '__main__':
    main()


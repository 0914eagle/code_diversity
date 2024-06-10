
def get_message_counts(n, k, message_links):
    # Initialize a set to store the seen messages
    seen_messages = set()
    # Initialize a queue to store the current message and its depth
    queue = [(1, 0)]
    # Initialize a dictionary to store the message counts
    message_counts = {}

    while queue:
        # Get the current message and its depth from the queue
        message, depth = queue.pop(0)
        # If the message is not seen before, mark it as seen and update the message counts
        if message not in seen_messages:
            seen_messages.add(message)
            message_counts[message] = depth
        # If the message has a link, add the linked message to the queue with an updated depth
        if message_links[message - 1] != 0:
            queue.append((message_links[message - 1], depth + 1))

    # Return the message counts
    return message_counts

def main():
    # Read the input n, k, and message links from stdin
    n, k = map(int, input().split())
    message_links = list(map(int, input().split()))
    # Call the get_message_counts function and print the results
    message_counts = get_message_counts(n, k, message_links)
    for i in range(1, n + 1):
        print(message_counts[i])

if __name__ == '__main__':
    main()


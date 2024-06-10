
def get_message_history(n, k, message_links):
    # Initialize a set to store the visited messages
    visited_messages = set()
    # Initialize a queue to store the messages to be processed
    queue = []
    # Add the starting message to the queue
    queue.append(n)
    # Loop until the queue is empty
    while queue:
        # Get the current message from the queue
        current_message = queue.pop(0)
        # If the current message has not been visited before, mark it as visited and add it to the set
        if current_message not in visited_messages:
            visited_messages.add(current_message)
        # Get the link for the current message
        link = message_links[current_message]
        # If the link is not zero, add the linked message to the queue
        if link != 0:
            queue.append(link)
    # Return the number of distinct messages visited
    return len(visited_messages)

def main():
    n, k = map(int, input().split())
    message_links = list(map(int, input().split()))
    result = []
    for i in range(1, n+1):
        result.append(get_message_history(i, k, message_links))
    print(*result, sep='\n')

if __name__ == '__main__':
    main()


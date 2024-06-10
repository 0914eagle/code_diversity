
def get_messages_to_read(n, k, messages):
    # Initialize a set to store the messages that have been read
    read_messages = set()
    # Initialize a queue to store the messages to process
    queue = []
    # Add the first message to the queue
    queue.append(messages[0])
    # Loop until the queue is empty
    while queue:
        # Get the current message from the queue
        current_message = queue.pop(0)
        # If the current message has not been read before, read it and add it to the set of read messages
        if current_message not in read_messages:
            read_messages.add(current_message)
            # Add the previous k messages to the queue
            for i in range(1, k + 1):
                previous_message = current_message - i
                if previous_message >= 0 and previous_message not in read_messages:
                    queue.append(previous_message)
            # Add the next k messages to the queue
            for i in range(1, k + 1):
                next_message = current_message + i
                if next_message <= n and next_message not in read_messages:
                    queue.append(next_message)
    # Return the number of distinct messages that have been read
    return len(read_messages)

def main():
    n, k = map(int, input().split())
    messages = list(map(int, input().split()))
    result = [0] * (n + 1)
    for i in range(n + 1):
        result[i] = get_messages_to_read(n, k, messages[:i])
    print(*result, sep='\n')

if __name__ == '__main__':
    main()


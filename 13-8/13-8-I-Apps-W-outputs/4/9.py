
def get_distinct_messages(messages, k):
    # Initialize a set to store the distinct messages
    distinct_messages = set()
    
    # Iterate through the messages
    for message in messages:
        # If the message is not already in the set, add it
        if message not in distinct_messages:
            distinct_messages.add(message)
        # If the message has a link, add the linked message to the set
        if message in links:
            distinct_messages.add(links[message])
    
    # Return the number of distinct messages
    return len(distinct_messages)

def main():
    # Read the input
    n, k = map(int, input().split())
    messages = list(map(int, input().split()))
    
    # Create a dictionary to store the links
    links = {}
    for i in range(n):
        if messages[i] != 0:
            links[i] = messages[i] - 1
    
    # Call the function to get the number of distinct messages
    result = get_distinct_messages(messages, k)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()


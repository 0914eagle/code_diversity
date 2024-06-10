
def get_leader(n, m):
    # Initialize a set to store the present members
    present = set()
    
    # Iterate through the messages
    for message in m:
        # If the message is a log on message, add the person to the set
        if message.startswith("+"):
            present.add(int(message[1:]))
        # If the message is a log off message, remove the person from the set
        elif message.startswith("-"):
            present.remove(int(message[1:]))
    
    # Return the size of the set
    return len(present)

def main():
    # Read the number of team participants and messages
    n, m = map(int, input().split())
    
    # Read the messages
    messages = [input() for _ in range(m)]
    
    # Call the get_leader function and print the result
    print(get_leader(n, messages))

if __name__ == '__main__':
    main()


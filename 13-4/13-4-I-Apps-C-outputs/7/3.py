
def get_leader(n, m, messages):
    # Initialize a set to store the present participants
    present = set()
    
    # Iterate through the messages
    for message in messages:
        # If the message is a log on message, add the participant to the set
        if message[0] == "+":
            present.add(int(message[1:]))
        # If the message is a log off message, remove the participant from the set
        elif message[0] == "-":
            present.remove(int(message[1:]))
    
    # Return the number of participants in the set
    return len(present)

def main():
    # Read the number of participants and messages
    n, m = map(int, input().split())
    
    # Read the messages
    messages = [input() for _ in range(m)]
    
    # Call the get_leader function and print the result
    print(get_leader(n, m, messages))

if __name__ == '__main__':
    main()


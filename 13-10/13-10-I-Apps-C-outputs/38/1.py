
def get_leaders(n, messages):
    # Initialize a set to store the leaders
    leaders = set()
    # Initialize a set to store the participants
    participants = set(range(1, n + 1))
    # Iterate over the messages
    for message in messages:
        # If the message is a log on message, add the participant to the leaders set
        if message.startswith("+"):
            leaders.add(int(message[1:]))
        # If the message is a log off message, remove the participant from the leaders set
        elif message.startswith("-"):
            leaders.remove(int(message[1:]))
        # If the leaders set is empty, return 0
        if not leaders:
            return 0
    # Return the number of leaders
    return len(leaders)

def main():
    # Read the input
    n, m = map(int, input().split())
    messages = [input() for _ in range(m)]
    # Get the leaders
    leaders = get_leaders(n, messages)
    # Print the number of leaders
    print(leaders)
    # If there are leaders, print them in increasing order
    if leaders:
        print(*sorted(leaders))

if __name__ == '__main__':
    main()


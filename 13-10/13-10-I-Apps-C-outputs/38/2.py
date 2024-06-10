
def is_leader(team_size, message_log):
    # Initialize a set to store the present members of the team
    present_members = set()
    
    # Iterate through the message log
    for message in message_log:
        # If the message is a log on message, add the corresponding member to the set of present members
        if message.startswith("+"):
            present_members.add(int(message[1:]))
        # If the message is a log off message, remove the corresponding member from the set of present members
        elif message.startswith("-"):
            present_members.remove(int(message[1:]))
    
    # Return the number of members in the set of present members, which is the number of possible leaders
    return len(present_members)

def find_leaders(team_size, message_log):
    # Find the number of possible leaders
    num_leaders = is_leader(team_size, message_log)
    
    # Initialize an empty list to store the numbers of the possible leaders
    leaders = []
    
    # Iterate through the message log
    for message in message_log:
        # If the message is a log on message and the corresponding member is present in the set of present members, add their number to the list of possible leaders
        if message.startswith("+") and int(message[1:]) in present_members:
            leaders.append(int(message[1:]))
    
    # Sort the list of possible leaders in increasing order and return it
    return sorted(leaders)

def main():
    # Read the input data
    team_size, num_messages = map(int, input().split())
    message_log = [input() for _ in range(num_messages)]
    
    # Find the numbers of the possible leaders
    leaders = find_leaders(team_size, message_log)
    
    # Print the number of possible leaders
    print(len(leaders))
    
    # Print the numbers of the possible leaders in increasing order
    print(*leaders)

if __name__ == '__main__':
    main()


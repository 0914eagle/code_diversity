
def solve_gift_giving_problem(n, friends):
    # Initialize a dictionary to map each friend to their gift receiver
    gift_receivers = {}
    
    # Iterate through the input friends and their gift preferences
    for i, friend in enumerate(friends):
        # If the friend has a gift preference, add them to the dictionary with their gift receiver
        if friend != 0:
            gift_receivers[i] = friend
    
    # Initialize a set to keep track of friends who have not been paired yet
    unpaired_friends = set(range(1, n+1))
    
    # While there are still unpaired friends, iterate through the dictionary and find pairs for them
    while unpaired_friends:
        for friend, receiver in gift_receivers.items():
            # If the receiver has not been paired yet, and the friend has not been paired yet, pair them together
            if receiver in unpaired_friends and friend in unpaired_friends:
                unpaired_friends.remove(receiver)
                unpaired_friends.remove(friend)
                gift_receivers[friend] = receiver
                gift_receivers[receiver] = friend
    
    # Return the gift receiver dictionary as the output
    return gift_receivers


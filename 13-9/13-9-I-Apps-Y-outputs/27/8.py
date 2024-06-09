
def solve(n, friends):
    # Initialize a dictionary to map each friend to their gift recipient
    gift_map = {}
    
    # Iterate through the list of friends and their gift preferences
    for i, friend in enumerate(friends):
        # If the friend has a gift preference, add them to the dictionary
        if friend != 0:
            gift_map[i] = friend
    
    # While there are still unknown gift preferences
    while 0 in gift_map.values():
        # Find the first friend who doesn't have a gift preference
        unknown_friend = [k for k, v in gift_map.items() if v == 0][0]
        
        # Find all friends who have gift preferences and are not their own gift recipient
        available_friends = [k for k, v in gift_map.items() if v != 0 and k != unknown_friend]
        
        # Assign the first available friend as the gift recipient for the unknown friend
        gift_map[unknown_friend] = available_friends[0]
    
    # Return the final gift map
    return gift_map

